#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
let data;
let person;
const listPerson = [];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    data = JSON.parse(body);
    data.characters.forEach(actor => {
      request(actor, function (error, response, body) {
        if (error) {
          console.log("Failed at id : " + actor);
          console.log(error);
        } else {
          person = JSON.parse(body);
          console.log(person.name);
        }
      });
    });
  }
});
