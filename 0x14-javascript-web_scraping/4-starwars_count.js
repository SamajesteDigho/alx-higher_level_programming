#!/usr/bin/node

const url = process.argv[2];
const userId = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

fetch(url).then((response) => {
  return response.json();
}).then((data) => {
  data.results.forEach(film => {
    if (film.characters.includes(userId)) {
      count++;
    }
  });
  console.log(count);
});
