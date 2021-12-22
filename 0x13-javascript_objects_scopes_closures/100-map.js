#!/usr/bin/node
const myArr = require('./100-data.js').list;
console.log(myArr);
console.log(myArr.map((element, index) => element * index));
