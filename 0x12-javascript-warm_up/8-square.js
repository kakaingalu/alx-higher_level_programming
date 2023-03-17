#!/usr/bin/node
// a script that prints a square.
const size = parseInt(process.argv[2], 10);

if (!size) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let newVar = '';
    for (let j = 0; j < size; j++) {
      newVar = newVar + 'X';
    }
    console.log(newVar);
  }
}
