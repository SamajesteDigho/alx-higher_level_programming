#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const path = process.argv[3];
let text;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    text = body;
    fs.writeFile(path, text, (err) => {
      if (err) throw console.log(err);
    });
  }
});
