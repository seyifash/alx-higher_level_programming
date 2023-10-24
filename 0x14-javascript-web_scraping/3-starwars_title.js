#!/usr/bin/node
const request = require('request');
const args = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${args}`;
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
