$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (myData) {
    $.each(myData.results, function (i, film) {
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  });
});
