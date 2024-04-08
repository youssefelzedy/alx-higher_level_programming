#!/usr/bin/node

const request = require('request');

const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
  method: 'GET'
};

request(options, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
