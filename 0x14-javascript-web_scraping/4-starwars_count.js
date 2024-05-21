#!/usr/bin/node
// JavaScript that prints the number of movies “Wedge Antilles”
const httpRequest = require('request');
if (process.argv.length > 2) {
  httpRequest(`${process.argv[2]}`, (error, httpResp, httpContent) => {
    if (error) {
      console.log(error);
    } else if (httpContent) {
      const movie = JSON.parse(httpContent).results.filter(
        k => k.characters.find(t => t.match(/\/people\/18\/?$/))
      );
      console.log(movie.length);
    }
  });
}
