#!/usr/bin/node
const request = require('request');
let url = 'http://swapi.co/api/films/:id' + process.argv[2];
request(url, function (error, response, body) {
    console.log(error || JSON.parse(body).title);
});
