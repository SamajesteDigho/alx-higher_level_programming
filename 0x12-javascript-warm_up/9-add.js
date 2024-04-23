#!/usr/bin/node

const args = process.argv;
const nb1 = parseInt(args[2]);
const nb2 = parseInt(args[3]);

function add (a, b) {
  return a + b;
}

console.log(add(nb1, nb2));
