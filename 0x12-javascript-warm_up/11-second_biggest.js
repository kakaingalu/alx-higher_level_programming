#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments.
if (process.argv[2] === 0 || process.argv.length <= 3) {
  console.log(0);
} else {
  process.argv.slice(2, process.argv.length);
  process.argv.sort(function (a, b) { return a - b; });
  console.log(process.argv[process.argv.length - 2]);
}
