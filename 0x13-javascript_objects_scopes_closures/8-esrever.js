#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    reversedList[list.length - 1 - i] = list[i];
  }

  return reversedList;
};
