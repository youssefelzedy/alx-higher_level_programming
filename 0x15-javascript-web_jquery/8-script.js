$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(character) {
    for (let i = 0; i < character.results.length; i++) {
        $('UL#list_movies').append('<li>' + character.results[i].title + '</li>');
    }
});