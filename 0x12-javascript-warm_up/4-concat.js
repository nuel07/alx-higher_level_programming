#!/usr/bin/node
const myConcator = ' is ';
const myArgs = process.argv.slice(2);
if (myArgs[0] === undefined && myArgs[1] === undefined) {
  console.log('undefined' + myConcator + 'undefined');
} else if (myArgs[0] !== undefined && myArgs[1] === undefined) {
  console.log(myArgs[0] + myConcator + 'undefined');
} else if (myArgs[0] !== undefined && myArgs[1] !== undefined) {
  console.log(myArgs[0] + myConcator + myArgs[1]);
} else if (myArgs[0] === undefined && myArgs[1] !== undefined) {
  console.log('undefined' + myConcator + myArgs[1]);
}
