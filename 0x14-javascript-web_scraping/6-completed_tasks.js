#!/usr/bin/node
// a script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.error(err);
  const data = JSON.parse(body);
  const jabs = {};
  for (let n = 0; n < data.length; n++) {
    if (data[n].completed === true) {
      if (!jabs[data[n].userId]) {
        jabs[data[n].userId] = 0;
      }
      jabs[data[n].userId] += 1;
    }
  }
  console.log(jabs);
});
