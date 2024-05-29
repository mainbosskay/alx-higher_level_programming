// JavaScript that adds the class red to the header when user clicks on tag
'use strict';
$(() => {
  $('DIV#red_header').click(() => {
    if (!$('header').hasClass('red')) {
      $('header').addClass('red');
    }
  });
});
