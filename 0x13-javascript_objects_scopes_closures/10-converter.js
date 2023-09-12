#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase (num) {
    return (
      num === 0
        ? '0'
        : (num < base
            ? num.toString(base)
            : convertToBase(~~(num / base)) + (num % base).toString(base))
    );
  };
};
