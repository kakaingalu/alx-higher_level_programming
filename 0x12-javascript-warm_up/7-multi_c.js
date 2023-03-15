#!/usr/bin/node
// a script that prints x times “C is fun”.
let i = 0;
if (!parseInt(process.argv[2], 10)) {
  console.log('Missing number of occurrences');
} else {
  while (i < process.argv[2]) {
    console.log('C is fun');
    i++;
  }
}
