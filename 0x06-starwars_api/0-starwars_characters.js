#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: 0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Unexpected status code: ${response.statusCode}`);
    process.exit(1);
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  const printCharacters = (charactersUrls) => {
    if (charactersUrls.length === 0) {
      return;
    }

    const characterUrl = charactersUrls.shift();
    request.get(characterUrl, (error, response, body) => {
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
      printCharacters(charactersUrls);
    });
  };

  printCharacters(charactersUrls);
});