#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const moviesData = JSON.parse(body);
    const count = moviesData.results.reduce((acc, movie) => {
      if (movie.characters.some(character => character.endsWith('/18/'))) {
        return acc + 1;
      }
      return acc;
    }, 0);
    console.log(`${count}`);
  }
});
