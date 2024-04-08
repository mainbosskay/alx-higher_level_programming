#!/usr/bin/node
const digts = Number.parseInt(process.argv[2]);
console.log(Number.isNaN(digts) ? 'Not a number' : 'My number: ' + digts);
