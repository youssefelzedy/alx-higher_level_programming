$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(character) {
    $('#character').text(character.name);
});