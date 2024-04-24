#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};

for (const elt in dict) {
  if (newDict[dict[elt]]) {
    newDict[dict[elt]].push(elt);
  } else {
    newDict[dict[elt]] = [elt];
  }
}

console.log(newDict);
