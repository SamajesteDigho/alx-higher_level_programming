#!/usr/bin/node

const SquareE = require('./5-square.js');

class Square extends SquareE {
  charPrint (c) {
    let filler, i, j;
    let str = '';
    if (c) {
      filler = c;
    } else {
      filler = 'X';
    }
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        str += filler;
      }
      if (i + 1 < this.height) {
        str += '\n';
      }
    }
    console.log(str);
  }
}

module.exports = Square;
