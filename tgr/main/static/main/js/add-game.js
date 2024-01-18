async function getIGDBGame() {
    $('form')[0].reset();
    const id = document.getElementById('search-game').value;
    if (!id) {
        alert('É necessário informar o ID do jogo!');
        return;
    }
    const selectGameMode = document.getElementById('id_players_mode');
    let game = null;
    try {
        const response = await fetch(
            `http://localhost:8000/get-igdb-game/${id}`,
        );

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }
    
        const gameData = await response.json();
        game = gameData[0];

        // Preenchendo os campos do formulário com as informações retornadas da API

        // Title
        $('#id_title').val(game.name);

        // IGDB ID
        $('#id_igdb_id').val(game.id);

        // Genres
        $.each(game.genres, function(index, genre) {
            var opcao = $('#id_genres option:contains("' + genre.name + '")').filter(function() {
                return $(this).text() === genre.name;
            });

            if (opcao.length > 0) {
                opcao.prop('selected', true);
            }
        });

        // Platforms
        $.each(game.platforms, function(index, platform) {
            var opcao = $('#id_platforms option:contains("' + platform.name + '")').filter(function() {
                return $(this).text() === platform.name;
            });

            if (opcao.length > 0) {
                opcao.prop('selected', true);
            }
        });

        // Players mode
        $.each(game.game_modes, function(index, gameMode) {
            var opcao = $('#id_players_mode option:contains("' + gameMode.name + '")').filter(function() {
                return $(this).text() === gameMode.name;
            });

            if (opcao.length > 0) {
                opcao.prop('selected', true);
            }
        });


        // Synopsis
        $('#id_synopsis').val(game.summary);

        // Wiki
        $('#id_wiki').val(game.url);

        // scroll para #save-game usando jquery
        $('html, body').animate({
            scrollTop: $("#save-game").offset().top
        }, 100);
        
    } catch (err) {
        console.error(err);
    }
}