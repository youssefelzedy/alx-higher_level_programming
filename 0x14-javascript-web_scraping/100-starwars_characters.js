#!/usr/bin/node

const request = require('request');

const options = {
  url: 'https://swapi.dev/api/films/' + process.argv[2] + '/',
  method: 'GET'
};

request(options, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const data = JSON.parse(body);
  const characters = data.characters;

  for (const character of characters) {
    request(character, (err, res, body) => {
      if (err) {
        return console.log(err);
      }
      const data = JSON.parse(body);
      console.log(data.name);
    });
  }
});
