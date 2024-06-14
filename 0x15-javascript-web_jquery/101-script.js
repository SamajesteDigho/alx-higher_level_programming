#!/usr/bin/node
// Add, Remove and Clear li items from ul
window.onload = function () {
  document.querySelector('DIV#add_item').addEventListener('click', function () {
    const li = document.createElement('li');
    li.textContent = 'Item';
    document.querySelector('UL.my_list').appendChild(li);
  });

  document.querySelector('DIV#remove_item').addEventListener('click', function () {
    const lc = document.querySelector('UL.my_list').lastChild;
    if (lc) {
      document.querySelector('UL.my_list').removeChild(lc);
    }
  });

  document.querySelector('DIV#clear_list').addEventListener('click', function () {
    while (document.querySelector('UL.my_list').children.length > 0) {
      const lc = document.querySelector('UL.my_list').lastChild;
      if (lc) {
        document.querySelector('UL.my_list').removeChild(lc);
      }
    }
  });
}
