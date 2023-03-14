#!/usr/bin/node
// a function that returns the reversed version of a list:
exports.esrever = function (list) {
  const reversedList = [];
  let len = list.length - 1;
  while (len >= 0) {
    reversedList.push(list[len]);
    len--;
  }
  return reversedList;
};
