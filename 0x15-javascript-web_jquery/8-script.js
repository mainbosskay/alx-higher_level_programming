// JavaScript that fetches and lists the title for all movies by using API URL
'use strict';
$(() => {
  const APIURL = 'https://swapi-api.hbtn.io/api';
  $.get(`${APIURL}/films/?format=json`, (moviedata, status) => {
    moviedata.results.forEach(movie => {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    });
  });
});
