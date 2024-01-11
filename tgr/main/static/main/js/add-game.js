async function getIGDBGame() {
    const id = document.getElementById('search-game').value;
    try {
        const response = await fetch(
            `http://localhost:8000/get-igdb-game/${id}`,
        );

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }
    
        const gameData = await response.json();
        console.log(gameData[0]);
    } catch (err) {
        console.error(err);
    }
}