#!/usr/bin/node
// Search translation on click and on enter press
window.onload = function () {
  $('INPUT#btn_translate').on('click', function () {
    lang = $('INPUT#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, function (data, status) {
      $('DIV#hello').text(data.hello);
    });
  });

  $('INPUT#language_code').on('keypress', function (e) {
    if (e.which == 13) {
      lang = $('INPUT#language_code').val();
      $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, function (data, status) {
        $('DIV#hello').text(data.hello);
      });
    }

  });
}