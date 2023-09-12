#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase (num) {
    if (num === 0) return '0';

    let result = '';
    while (num > 0) {
      result = (num % base).toString(base) + result;
      num = Math.floor(num / base);
    }

    return result;
  };
};
