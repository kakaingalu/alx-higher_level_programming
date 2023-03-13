#!/usr/bin/node
// a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer.
let i = 0;
if (!parseInt(process.argv[2], 10)) {
  console.log('Missing number of occurrences');
} else {
  while (i < process.argv[2]) {
    console.log('C is fun');
    i++;
  }
}
