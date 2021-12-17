#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  let l = 0;  
  while (l < list.length-1) {
    rev.push(list.pop);
  }
  return rev;
};
