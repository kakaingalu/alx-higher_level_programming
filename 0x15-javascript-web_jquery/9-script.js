$(document).ready(() => {
  const transUrl = 'https://fourtonfish.com/hellosalut/?lang=fr';
  let results = null;

  $.ajax({
    url: transUrl,
    method: 'GET',
    async: false,
    success: (myData) => {
      results = myData.hello;
    },
    error: () => {
      results = 'Error fetching data';
    }
  });

  if (results) {
    $('#hello').text(results);
  }
});
