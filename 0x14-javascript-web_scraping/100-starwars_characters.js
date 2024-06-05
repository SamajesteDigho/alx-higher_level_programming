#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
let data;
let person;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    data = JSON.parse(body);
    data.characters.forEach(actor => {
      request(actor, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          person = JSON.parse(body);
          console.log(person.name);
        }
      });
    });
  }
});
