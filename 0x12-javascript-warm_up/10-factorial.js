#!/usr/bin/node
// a script that computes and prints a factorial
const f = Number(process.argv[2]);
function factorial (f) {
  if (f === 0 || isNaN(f)) {
    return 1;
  } else {
    return (f * (factorial(f - 1)));
  }
}

console.log(factorial(f));
