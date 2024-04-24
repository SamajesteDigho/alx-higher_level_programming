#!/usr/bin/node

const list = require('./100-data.js').list;

const array = list.map((a, i) => a * i);
console.log(list);
console.log(array);
