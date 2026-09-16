#!/usr/bin/env node
/*
 * Dependency-free runtime smoke test for the standalone PULSE OBG app.
 * It runs the inline application script against a minimal DOM shim, then checks
 * the roadmap and a live Chapter 10 quiz flow. It complements the structural
 * checks in check_integrity.py; it is not intended as a visual-browser test.
 */
'use strict';

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const appPath = path.join(__dirname, 'pulse-obg.html');
const html = fs.readFileSync(appPath, 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) throw new Error('No inline application script found.');

class FakeClassList {
  constructor() { this.values = new Set(); }
  add(...values) { values.forEach((value) => this.values.add(value)); }
  remove(...values) { values.forEach((value) => this.values.delete(value)); }
  toggle(value, force) {
    if (force === true) { this.add(value); return true; }
    if (force === false) { this.remove(value); return false; }
    if (this.values.has(value)) { this.remove(value); return false; }
    this.add(value);
    return true;
  }
  contains(value) { return this.values.has(value); }
}

class FakeElement {
  constructor(tagName = 'div') {
    this.tagName = tagName;
    this.classList = new FakeClassList();
    this.style = {};
    this.children = [];
    this.textContent = '';
    this.disabled = false;
    this.onclick = null;
    this._innerHTML = '';
  }
  set innerHTML(value) {
    this._innerHTML = String(value);
    this.children = [];
  }
  get innerHTML() { return this._innerHTML; }
  appendChild(child) { this.children.push(child); return child; }
  querySelector() { const child = new FakeElement(); this.appendChild(child); return child; }
  getBoundingClientRect() { return { left: 0, top: 0, width: 100 }; }
  remove() {}
}

const elements = new Map();
for (const match of html.matchAll(/id="([^"]+)"/g)) {
  elements.set(match[1], new FakeElement());
}
for (const match of scriptMatch[1].matchAll(/\$\('([^']+)'\)/g)) {
  if (!elements.has(match[1])) elements.set(match[1], new FakeElement());
}

const document = {
  body: new FakeElement('body'),
  getElementById(id) {
    if (!elements.has(id)) elements.set(id, new FakeElement());
    return elements.get(id);
  },
  createElement(tagName) { return new FakeElement(tagName); },
  addEventListener() {},
};
const localStorage = {
  values: new Map(),
  getItem(key) { return this.values.has(key) ? this.values.get(key) : null; },
  setItem(key, value) { this.values.set(key, String(value)); },
};
const context = {
  document, localStorage, console, Math, Date, setTimeout: () => {},
  window: { scrollY: 0 },
};
vm.createContext(context);
vm.runInContext(`${scriptMatch[1]}

globalThis.__PULSE_SMOKE__ = {
  QUESTIONS, UNITS, CHAPTERS, QBYID, unitsOf,
  chapters() { renderChapters(); },
  path(number) { curCh = number; renderPath(); },
  start(number) { curCh = number; curUnit = unitsOf(number)[0]; beginUnit(); return curUnit; }
};`, context, { filename: appPath });

const pulse = context.__PULSE_SMOKE__;
function assert(condition, message) {
  if (!condition) throw new Error(message);
}

// Expectations are derived from the chapter source artifacts in data/, so the
// smoke test never drifts when questions are added or reordered.
const dataDir = path.join(__dirname, 'data');
const source = fs
  .readdirSync(dataDir)
  .filter((name) => /^ch\d{2}\.json$/.test(name))
  .sort()
  .map((name) => JSON.parse(fs.readFileSync(path.join(dataDir, name), 'utf8')));
const sourceQuestions = source.flatMap((chapter) => chapter.questions);
const sourceUnits = source.flatMap((chapter) => chapter.units);
const lastId = (number) => sourceQuestions.filter((q) => q.id.startsWith(`OBG-C${number}-`)).pop().id;
const unitCount = (number) => sourceUnits.filter((u) => u.ch === number).length;
const firstUnitSize = (number) => sourceUnits.find((u) => u.ch === number && u.n === 1).qs.length;

assert(pulse.QUESTIONS.length === sourceQuestions.length,
  `Expected ${sourceQuestions.length} questions, found ${pulse.QUESTIONS.length}.`);
assert(pulse.UNITS.length === sourceUnits.length,
  `Expected ${sourceUnits.length} units, found ${pulse.UNITS.length}.`);
assert(pulse.CHAPTERS.filter((chapter) => chapter.live).length === 24, 'Expected 24 live chapters.');

pulse.chapters();
assert(elements.get('chList').children.length === 24, 'Roadmap did not render 24 chapter rows.');
assert(elements.get('chList').children[5].innerHTML.includes(`${unitCount(6)} units`), 'Chapter 6 unit total did not render.');

pulse.path(10);
assert(pulse.unitsOf(10).length === unitCount(10), `Chapter 10 unit lookup did not return ${unitCount(10)} units.`);
assert(elements.get('pathTitle').textContent === pulse.CHAPTERS[9].t, 'Chapter 10 path title did not render.');

const firstUnit = pulse.start(10);
assert(firstUnit.id === 'OBG-U10-1', 'Chapter 10 first unit did not start.');
assert(elements.get('qcount').textContent === `QUESTION 1 OF ${firstUnitSize(10)}`, 'Quiz count did not render the Chapter 10 unit.');
assert(elements.get('qtext').textContent.length > 20, 'Quiz did not render a question stem.');
assert(elements.get('opts').children.length === 4, 'Quiz did not render four options.');
assert(pulse.QBYID[lastId(10)].page === 441, `Final Chapter 10 question ${lastId(10)} is unavailable.`);

pulse.path(15);
assert(pulse.unitsOf(15).length === unitCount(15), `Chapter 15 unit lookup did not return ${unitCount(15)} units.`);
assert(elements.get('pathTitle').textContent === pulse.CHAPTERS[14].t, 'Chapter 15 path title did not render.');
assert(pulse.QBYID[lastId(15)].page === 489, `Final Chapter 15 question ${lastId(15)} is unavailable.`);
pulse.path(24);
assert(pulse.unitsOf(24).length === unitCount(24), `Chapter 24 unit lookup did not return ${unitCount(24)} units.`);
assert(elements.get('pathTitle').textContent === pulse.CHAPTERS[23].t, 'Chapter 24 path title did not render.');
const lastUnit = pulse.start(24);
assert(lastUnit.id === 'OBG-U24-1', 'Chapter 24 first unit did not start.');
assert(elements.get('opts').children.length === 4, 'Chapter 24 quiz did not render four options.');
assert(pulse.QBYID[lastId(24)].page === 572, `Final Chapter 24 question ${lastId(24)} is unavailable.`);
assert(pulse.QBYID[lastId(19)].page === 527, `Final Chapter 19 question ${lastId(19)} is unavailable.`);

console.log('PASS: roadmap, Chapter 6/10/15/24 path data, Chapter 10/24 quiz starts, and final Chapter 10/15/19/24 questions render at runtime.');
