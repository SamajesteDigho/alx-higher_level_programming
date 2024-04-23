#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    let i, j;
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        str += 'X';
      }
      if (i + 1 < this.height) {
        str += '\n';
      }
    }
    console.log(str);
  }
}

module.exports = Rectangle;
