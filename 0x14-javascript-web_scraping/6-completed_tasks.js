#!/usr/bin/node

const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET',
  json: true
};

request(options, (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  const tasksCompleted = {};

  body.forEach((todo) => {
    if (todo.completed === true) {
      if (tasksCompleted[todo.userId] === undefined) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId]++;
      }
    }
  });
  console.log(tasksCompleted);
});
