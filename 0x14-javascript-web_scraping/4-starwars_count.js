#!/usr/bin/node

const request = require('request');
let count = 0;

const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/',
  method: 'GET'
};

request(options, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const data = JSON.parse(body);
  data.results.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes('18')) {
        count++;
      }
    });
  });
  console.log(count);
});
