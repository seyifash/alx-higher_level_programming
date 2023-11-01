#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, response, body) {
  if (!err) {
    const todos = JSON.parse(body);
    const completed = {};
    for (let i = 0; i < todos.length; i++) {
      const todo = todos[i];
      if (todo.completed === true) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId]++;
        }
      }
    }
    console.log(completed);
  }
});
