#!/usr/bin/node
// Toggle color change on click
let color;
$('DIV#toggle_header').on('click', function () {
  color = $('header').attr('class');
  if (color === 'red') {
    color = 'green';
  } else {
    color = 'red';
  }
  $('header').removeAttr('class');
  $('header').addClass(color);
});
