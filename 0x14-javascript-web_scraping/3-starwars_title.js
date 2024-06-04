#!/usr/bin/node

const epn = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + epn;

fetch(url).then((response) => {
  return response.json();
}).then((data) => {
  console.log(data.title);
});
