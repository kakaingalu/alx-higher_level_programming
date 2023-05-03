#!/usr/bin/node
//  a JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (myData) => {
  $('DIV#character').text(myData.name)
  }));
}));
