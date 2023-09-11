#!/usr/bin/bash
exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
