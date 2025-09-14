document.addEventListener("DOMContentLoaded", () => {
    fetch("/static/data/filmes.json")
        .then(response => response.json())
        .then(filmes => {
            const dashboard = document.getElementById("dashboard");


            filmes.forEach(filme => {
                const card = document.createElement("div");
                card.classList.add("card");


                card.innerHTML = `
                    <img src="/static/img/${filme.poster}" alt="${filme.titulo}">
                    <h3>${filme.titulo}</h3>
                    <p>Gênero: ${filme.genero}</p>
                    <p>Nota: <span class="nota">${filme.nota}</span></p>
                    <p>Data de lançamento: ${filme.lancamento}</p>
                `;


                dashboard.appendChild(card);
            });
        })
        .catch(err => console.error("Erro ao carregar filmes:", err));
});


    