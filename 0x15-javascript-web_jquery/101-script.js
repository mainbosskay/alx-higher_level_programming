// JavaScript that adds, removes and clears LI elements from a list when the user clicks
'use strict';
$(() => {
  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(() => {
    const listelem = $('UL.my_list').children().last();
    if (listelem) {
      listelem.remove();
    }
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list').empty();
  });
});
