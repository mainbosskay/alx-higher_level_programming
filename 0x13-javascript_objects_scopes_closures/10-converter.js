#!/usr/bin/node
exports.converter = function (base) {
  return function (digtToConvt) {
    return digtToConvt.toString(base);
  };
};
