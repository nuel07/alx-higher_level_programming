#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorial (x) {
  return x === 0 || isNaN(x) ? 1 : x * factorial(x - 1);
}
console.log(factorial(num));
