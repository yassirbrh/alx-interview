#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/films/';
const id = process.argv[2];
request.get(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    for (let i = 0; i < characters.length; i++) {
      request.get(characters[i], function (error, response, bodyCharacter) {
        if (error) {
          console.log(error);
        } else {
          const dataCharacter = JSON.parse(bodyCharacter);
          console.log(dataCharacter.name);
        }
      });
    }
  }
});

