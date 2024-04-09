#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let k = 0; k < this.height; k++) {
      let recgle = '';
      for (let t = 0; t < this.width; t++) {
        recgle += 'X';
      }
      console.log(recgle);
    }
  }
}
module.exports = Rectangle;
