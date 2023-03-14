#!/usr/bin/node
/*
a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

You must use the class notation for defining your class and extends
The constructor must take 1 argument: size
The constructor of Rectangle must be called (by using super())
*/
class Square extends require('./5-square') {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      console.log((c === undefined ? 'X' : c).repeat(this.width));
    }
  }
}

module.exports = Square;
