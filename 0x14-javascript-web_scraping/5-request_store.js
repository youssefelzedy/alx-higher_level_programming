#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const options = {
  url: process.argv[2]
};

request(options, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  fs.writeFile(process.argv[3], body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
