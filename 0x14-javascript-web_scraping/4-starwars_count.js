#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const userId = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;
let data;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    data = JSON.parse(body);
    data.results.forEach(film => {
      if (film.characters.includes(userId)) {
        count++;
      }
    });
    console.log(count);
  }
});
