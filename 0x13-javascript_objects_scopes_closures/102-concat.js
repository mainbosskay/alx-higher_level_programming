#!/usr/bin/node
const fSys = require('fs');
const frstArgCtnts = fSys.readFileSync(process.argv[2]).toString();
const secndArgCtnts = fSys.readFileSync(process.argv[3]).toString();
fSys.writeFileSync(process.argv[4], frstArgCtnts + secndArgCtnts);
