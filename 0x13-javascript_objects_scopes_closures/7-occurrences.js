#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((l, o) => o === searchElement ? l + 1 : l, 0);
};
