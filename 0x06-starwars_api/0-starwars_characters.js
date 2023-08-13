#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

if (args.length !== 1) {
  console.error('Usage: 0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = args[0];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Unexpected status code: ${response.statusCode}`);
    process.exit(1);
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        process.exit(1);
      }

      if (response.statusCode !== 200) {
        console.error(`Unexpected status code: ${response.statusCode}`);
        process.exit(1);
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});