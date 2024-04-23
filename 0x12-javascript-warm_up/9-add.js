#!/usr/bin/node

let args = process.argv;
let nb1 = parseInt(args[2]);
let nb2 = parseInt(args[3]);

function add (a, b) {
  return a + b;
}

console.log(add(nb1, nb2));
