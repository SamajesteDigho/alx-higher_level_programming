#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2]);
let str, i, j;
if (x) {
  for (i = 0; i < x; i++) {
    str = '';
    for (j = 0; j < x; j++) {
      str += 'X';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
