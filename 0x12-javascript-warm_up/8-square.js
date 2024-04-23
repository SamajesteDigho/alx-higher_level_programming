#!/usr/bin/node

let args = process.argv;
let x = parseInt(args[2]);
let str;

if (x) {
  for (i = 0; i < x; i++) {
    str = '';
    for (j = 0; j < x; j++) {
      str += 'x';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}