#!/usr/bin/node
// Colect film data and display in the ul
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  ul = $('UL#list_movies');
  data.results.forEach(film => {
    ul.append('<li>' + film.title + '</li>');
  });
});
