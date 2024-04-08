#!/usr/bin/node
function factorial (digts) {
  if (Number.isNaN(digts) || (digts <= 0)) {
    return 1;
  } else {
    return digts * factorial(digts - 1);
  }
}
console.log(factorial(Number.parseInt(process.argv[2])));
