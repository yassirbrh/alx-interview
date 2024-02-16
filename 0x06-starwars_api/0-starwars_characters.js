#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/films/';
const id = process.argv[2];
if (process.argv.length > 2) {
  request(url + id, (err, resp, body) => {
    if (err) {
      console.error(err);
      return;
    }

    try {
      const charactersURL = JSON.parse(body).characters;
      const charactersName = charactersURL.map(
        url => new Promise((resolve, reject) => {
          request(url, (promiseErr, promiseResp, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
              return;
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        }));

      Promise.all(charactersName)
        .then(names => console.log(names.join('\n')))
        .catch(allErr => console.error(allErr));
    } catch (parseErr) {
      console.error('Error parsing response:', parseErr);
    }
  });
}
