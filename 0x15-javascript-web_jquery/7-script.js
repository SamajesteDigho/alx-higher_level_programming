#!/usr/bin/node
// Fetch data with jquery get and display the name attribute
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, status) {
  $('DIV#character').text(data.name);
});
