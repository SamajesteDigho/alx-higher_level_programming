#!/usr/bin/node

let args = process.argv;
let arr = [];

for (i = 2; i < args.length; i++) {
  arr.push(parseInt(args[i]));
}

if (arr.length > 1) {
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
} else {
  console.log(0);
}
