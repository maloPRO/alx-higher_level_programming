#!/usr/bin/node

const Square1 = require('./5-square.js');

class Square extends Square1 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        for (let j = 0; j < this.size; j++) {
          process.stdout.write('C');
        }
        console.log();
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        for (let j = 0; j < this.size; j++) {
          process.stdout.write('X');
        }
        console.log();
      }
    }
  }
}

module.exports = Square;
