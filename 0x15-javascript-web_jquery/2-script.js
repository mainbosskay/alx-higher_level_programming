// JavaScript that updates the text color of header when user clicks on tag
'use strict';
$(() => {
  $('DIV#red_header').click(() => {
    $('header').css('color', '#FF0000');
  });
});
