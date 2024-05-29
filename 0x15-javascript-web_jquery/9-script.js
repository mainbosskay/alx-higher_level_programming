// JavaScript that fetches from API URL and displays the value of hello from that fetch in HTML tag
'use strict';
$(() => {
  const APIURL = 'https://fourtonfish.com';
  $.get(`${APIURL}/hellosalut/?lang=fr`, (hellodata, status) => {
    $('DIV#hello').html(hellodata.hello);
  });
});
