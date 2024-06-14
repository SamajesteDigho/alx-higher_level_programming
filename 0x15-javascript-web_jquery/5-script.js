#!/usr/bin/node
// Add li item on click
$('DIV#add_item').on('click', function () {
  $('UL.my_list').append("<li>Item</li>")
});
