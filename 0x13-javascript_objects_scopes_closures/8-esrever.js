#!/usr/bin/node
exports.esrever = function (list) {
  const myList = [];
  while (list.length > 0) {
    myList.push(list.pop());
  }
  return myList;
};
