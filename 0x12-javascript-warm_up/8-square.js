#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const ntimes = Number(process.argv[2]);
  let k = 0;
  while (k < ntimes) {
    console.log('X'.repeat(ntimes));
    k++;
  }
}
