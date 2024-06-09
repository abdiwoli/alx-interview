#!/usr/bin/node

const req = require('request');
const req1 = (array, el) => {
  if (el === array.length) return;
  req(array[el], (error, res, body) => {
    if (error) {
      throw error;
    } else {
      console.log(JSON.parse(body).name);
      req1(array, el + 1);
    }
  });
};

req(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (error, response, body) => {
    if (error) {
      throw error;
    } else {
      const chars = JSON.parse(body).characters;
      req1(chars, 0);
    }
  }
);
