#!/usr/bin/node
//  a script that prints a message depending of the number of arguments passed.
const argc = process.argv.length;

if (argc > 2) {
  console.log('Argument' + (argc > 3 ? 's' : '') + ' found');
} else {
  console.log('No argument');
}
