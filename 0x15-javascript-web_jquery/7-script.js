// JavaScript that fetches the character name from API URL
'use strict';
$(() => {
  const APIURL = 'https://swapi-api.hbtn.io/api';
  $.get(`${APIURL}/people/5/?format=json`, (charName, status) => {
    $('DIV#character').html(charName.name);
  });
})
