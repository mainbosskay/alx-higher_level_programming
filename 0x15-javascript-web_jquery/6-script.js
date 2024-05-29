// JavaScript that updates the text of the header to New Header when user clicks on tag
'use strict';
$(() => {
  $('DIV#update_header').click(() => {
    $('header').text('New Header!!!');
  });
});
