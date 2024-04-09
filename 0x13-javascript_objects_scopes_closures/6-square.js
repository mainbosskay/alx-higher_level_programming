#!/usr/bin/node
const SquareAncestor = require('./5-square');
class Square extends SquareAncestor {
  charPrint (c) {
    const chrprint = c === undefined ? 'X' : c;
    const horiztln = new Array(this.width).fill(chrprint, 0, this.width);
    const grndrows = new Array(this.height).fill(horiztln.join(''), 0, this.height);
    console.log(grndrows.join('\n'));
  }
}
module.exports = Square;
