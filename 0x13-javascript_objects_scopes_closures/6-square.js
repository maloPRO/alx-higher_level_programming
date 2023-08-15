#!/usr/bin/node

const Rectangle = require("./4-rectangle");

class Square extends Rectangle {
  constructor(size) {
    super(size);
    this.width = size;
    this.height = size;
  }
  charPrint(c) {
    if (c === undefined) {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          process.stdout.write("X");
        }
        console.log();
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          process.stdout.write(c);
        }
        console.log();
      }
    }
  }
}

module.exports = Square;
