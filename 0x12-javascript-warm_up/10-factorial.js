#!/usr/bin/node

let args = process.argv;
let nb = parseInt(args[2]);

function factorial (a) {
  if (a) {
    if (a == 0 || a == 1) {
      return 1;
    }
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}

console.log(factorial(nb));
