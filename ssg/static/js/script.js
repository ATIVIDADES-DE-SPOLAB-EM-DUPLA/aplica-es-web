document.addEventListener('DOMContentLoaded', function(){
    const botoes = document.querySelectorAll('.botao-detalhes')
    
    botoes.forEach(botao => {
        botao.addEventListener('click', function(){
            const resposta = this.nextElementSibling;

            if (resposta.style.display === 'block'){
                resposta.style.display = 'none';
                this.textContent = 'Detalhes';
            } else{
                resposta.style.display = 'block';
                this.textContent = 'Ocultar';
            }
        })
    })
})