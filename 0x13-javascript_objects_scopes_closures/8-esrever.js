#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (arr, p) {
    return arr.push(p);
  }, []);
};
