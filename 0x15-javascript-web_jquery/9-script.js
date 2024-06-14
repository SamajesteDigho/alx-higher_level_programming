#!/usr/bin/node
// Display text translation of hello
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, status) {
  $('DIV#hello').text(data.hello);
});
