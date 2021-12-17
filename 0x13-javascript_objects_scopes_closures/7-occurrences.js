#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  return list.reduce((l, o) => o === searchElement ? l + 1 : l, 0);
};
