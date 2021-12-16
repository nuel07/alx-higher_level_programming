#!/usr/bin/node
const myArgs = process.argv;
const myNum = parseInt(myArgs[2]);
console.log(isNaN(myNum) ? 'Not a number' : `My number: ${myNum}`);
