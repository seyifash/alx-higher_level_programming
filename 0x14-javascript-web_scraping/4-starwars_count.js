#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const moviesDat = JSON.parse(body);
    let count = 0;
    moviesDat.results.forEach((movie) => {
      if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });
    console.log(`${count}`);
  }
});
