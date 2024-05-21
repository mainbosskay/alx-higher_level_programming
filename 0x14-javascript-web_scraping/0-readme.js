#!/usr/bin/node
// JavaScript that reads and prints the content of a file
const fs = require('fs');
if (process.argv.length > 2) {
  fs.readFile(process.argv[2], (error, flcnt) => {
    if (error) {
      console.log(error);
    } else {
      console.log(flcnt.toString('utf-8'));
    }
  });
}
