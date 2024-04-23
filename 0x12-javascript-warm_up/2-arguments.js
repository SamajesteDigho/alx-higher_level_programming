#!/usr/bin/node

let nbArgs = process.argv.length

if (nbArgs < 3) {
  console.log('No argument');
} else if (nbArgs == 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
