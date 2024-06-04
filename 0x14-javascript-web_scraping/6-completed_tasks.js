#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
let data;
const result = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    data = JSON.parse(body);
    data.forEach(task => {
      if (task.completed) {
        if (result[task.userId]) {
          result[task.userId]++;
        } else {
          result[task.userId] = 1;
        }
      }
    });
    console.log(result);
  }
});
