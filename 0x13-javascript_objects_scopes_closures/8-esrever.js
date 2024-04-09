#!/usr/bin/node
exports.esrever = function (list) {
  const lengt = list.length;
  const revArr = new Array(lengt);
  list.forEach((element, indx) => {
    revArr[lengt - indx - 1] = element;
  });
  return revArr;
};
