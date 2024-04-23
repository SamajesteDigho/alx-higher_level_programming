#!/usr/bin/node

let args = process.argv;
let myNb = parseInt(args[2]);

if (myNb) {
  console.log(myNb);
}
else {
  console.log('Not a number');
}
