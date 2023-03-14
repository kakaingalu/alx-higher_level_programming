#!/usr/bin/node
// a function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let i = 0;

  while (i < list.length) {
    if (list[i] === searchElement) {
      count += 1;
    }
    i++;
  }

  return count;
};
