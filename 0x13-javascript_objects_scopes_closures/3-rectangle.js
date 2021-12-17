#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  // instance method
  print () {
    for (let x = 0; x < this.height; x++) {
      let row = '';
      for (let r = 0; r < this.height; r++) row += 'X';
      console.log(row);
    }
  }
};
