#!/usr/bin/node
// JavaScript that computes the number of tasks completed by user id
const httpRequest = require('request');
if (process.argv.length > 2) {
  httpRequest(process.argv[2], (error, httpResp, httpContent) => {
    const taskcnt = {};
    if (error) {
      console.log(error);
    }
    JSON.parse(httpContent).forEach(task => {
      if (task.completed) {
        if (!taskcnt[task.userId]) {
          taskcnt[task.userId] = 0;
        }
        taskcnt[task.userId]++;
      }
    });
    console.log(taskcnt);
  });
}
