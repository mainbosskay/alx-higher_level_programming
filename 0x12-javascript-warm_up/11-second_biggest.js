#!/usr/bin/node
const arg = process.argv
  .slice(2)
  .map(ag => Number.parseInt(ag))
  .sort((k, t) => t - k);
const the2 = arg.length < 2 ? 0 :arg[1];
console.log(the2);
