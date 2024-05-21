#!/usr/bin/node
// JavaScript that prints all characters of a Star Wars movie
const httpRequest = require('request');
const URL = 'https://swapi-api.hbtn.io/api';
if (process.argv.length > 2) {
  httpRequest(`${URL}/films/${process.argv[2]}/`, (error, httpResp, httpContent) => {
    if (error) {
      console.log(error);
    }
    const charURLs = JSON.parse(httpContent).characters;
    charURLs.forEach(task => {
      httpRequest(task, (error, httpResp, httpContent) => {
        if (error) {
          console.log(error);
        }
        console.log(JSON.parse(httpContent).name);
      });
    });
  });
}
