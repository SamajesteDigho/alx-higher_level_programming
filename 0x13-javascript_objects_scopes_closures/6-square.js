#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let filler, i, j;
    let str = '';
    if (c) {
      filler = c;
    } else {
      filler = 'X';
    }
    for (i = 0; i < this.size; i++) {
      for (j = 0; j < this.size; j++) {
        str += filler;
      }
      if (i + 1 < this.size) {
        str += '\n';
      }
    }
    console.log(str);
  }
}

module.exports = Square;
