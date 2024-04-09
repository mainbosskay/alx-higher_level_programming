#!/usr/bin/node
const dict = require('./101-data.js').dict;
const numdict = {};
Object.getOwnPropertyNames(dict).forEach(numOccr => {
  if (numdict[dict[numOccr]] === undefined) {
    numdict[dict[numOccr]] = [numOccr];
  } else {
    numdict[dict[numOccr]].push(numOccr);
  }
});
console.log(numdict);
