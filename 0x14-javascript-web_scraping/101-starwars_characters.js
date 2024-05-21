#!/usr/bin/node
// JavScript that prints all characters of a Star Wars movie
const httpRequest = require('request');
const URL = 'https://swapi-api.hbtn.io/api';
if (process.argv.length > 2) {
  httpRequest(`${URL}/films/${process.argv[2]}/`, (error, httpResp, httpContent) => {
    if (error) {
      console.log(error);
    }
    const charURLs = JSON.parse(httpContent).characters;
    const charNames = charURLs.map(
      url => new Promise((resolve, reject) => {
        httpRequest(url, (error, httpResp, httpContent) => {
          if (error) {
            reject(error);
          }
          resolve(JSON.parse(httpContent).name);
        });
      }));
    Promise.all(charNames)
      .then(names => console.log(names.join('\n')))
      .catch(error => console.log(error));
  });
}
