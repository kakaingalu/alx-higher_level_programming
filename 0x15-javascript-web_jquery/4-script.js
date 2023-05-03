#!/usr/bin/node
//a JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header

$(document).ready($('DIV#toggle_header').click(() => {
  $('header').toggleClass('red green')
}));
