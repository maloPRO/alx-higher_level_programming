#!/usr/bin/node

class Square extends require('./5-square.js') {
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
      this.print();
    }
  }
}

module.exports = Square;
