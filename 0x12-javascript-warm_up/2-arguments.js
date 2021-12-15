#!/usr/bin/node
const myArgs = process.argv.length;
if (myArgs > 1){
    console.log('Arguments found');
} else if (myArgs == 1){
    console.log('Argument found');
} else {
    console.log('No argument');
}
