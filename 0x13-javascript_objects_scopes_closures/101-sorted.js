#!/usr/bin/node
const dict = require('./101-data.js').dict;
const myDict = {};
for (const k in dict) {
  if (myDict[dict[k]] === undefined) {
    myDict[dict[k]] = [];
  }
  myDict[dict[k]].push(k);
}
console.log(myDict);
