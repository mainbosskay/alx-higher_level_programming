#!/usr/bin/node
// JavaScript that prints the title of a Star Wars movie
const httpRequest = require('request');
const URL = 'https://swapi-api.hbtn.io/api';
if (process.argv.length > 2) {
  httpRequest(`${URL}/films/${process.argv[2]}/`, (error, httpResp, httpContent) => {
    if (error) {
      console.log(error);
    }
    console.log(JSON.parse(httpContent).title);
  });
}
