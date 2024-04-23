#!/usr/bin/node

let args = process.argv;
let x = parseInt(args[2]);

if (x) {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
