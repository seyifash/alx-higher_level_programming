#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const taskData = JSON.parse(body);
  const completedTask = {};
  taskData.forEach((task) => {
    if (task.completed) {
      if (!completedTask[task.userId]) {
        completedTask[task.userId] = 1;
      } else {
        completedTask[task.userId]++;
      }
    }
  });
  for (const userId in completedTask) {
    console.log(`${userId}: ${completedTask[userId]}`);
  }
});
