#!/usr/bin/node
// Fetch hello translation on button click
window.onload = function () {
  $('INPUT#btn_translate').on('click', function () {
    lang = $('INPUT#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, function (data, status) {
      $('DIV#hello').text(data.hello);
    });
  });
}