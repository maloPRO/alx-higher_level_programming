#!/usr/bin/node

const Rectangle = require("./4-rectangle");

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }

  charPrint(c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write("C");
        }
        console.log();
      }
    }
  }
}

module.exports = Square;
