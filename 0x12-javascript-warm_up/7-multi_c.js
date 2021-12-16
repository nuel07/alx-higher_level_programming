#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let z = 0; z < x; z++) {
    console.log('C is fun');
  }
}
