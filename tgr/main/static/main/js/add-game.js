async function getIGDBGame() {
    const id = document.getElementById('search-game').value;
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
            // Encontre a opção com o texto correspondente ao nome do modo de jogo
            var opcao = $('#id_genres option:contains("' + genre.name + '")');
        
            // Se a opção existir, marque-a
            if (opcao.length > 0) {
                opcao.prop('selected', true);
            }
        });

        // Platforms
        $.each(game.platforms, function(index, platform) {
            // Encontre a opção com o texto correspondente ao nome do modo de jogo
            var opcao = $('#id_platforms option:contains("' + platform.name + '")');
        
            // Se a opção existir, marque-a
            if (opcao.length > 0) {
                opcao.prop('selected', true);
            }
        });

        // Players mode
        $.each(game.game_modes, function(index, gameMode) {
            // Encontre a opção com o texto correspondente ao nome do modo de jogo
            var opcao = $('#id_players_mode option:contains("' + gameMode.name + '")');
        
            // Se a opção existir, marque-a
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