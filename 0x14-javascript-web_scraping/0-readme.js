#!/usr/bin/node
// a script that reads and prints the content of a file

const fs = require('fs');
const fileP = process.argv[2];
fs.readFile(fileP, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
