#!/usr/bin/node

const args = process.argv;
const myNb = parseInt(args[2]);

if (myNb) {
  console.log('My number: ' + myNb);
} else {
  console.log('Not a number');
}
