from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mostrar_filmes():
    filmes = [
        {'classificação': '1', 'título': 'Invocação do Mal', 'nota': 7.5},
        {'classificação': '2', 'título': 'Invocação do Mal 2', 'nota': 7.3},
        {'classificação': '3', 'título': 'Faça Ela Voltar', 'nota': 7.2},
        {'classificação': '4', 'título': 'A Hora do Mal', 'nota': 7.1},
        {'classificação': '5', 'título': 'Os Caras Malvados 2', 'nota': 7.1},
        {'classificação': '6', 'título': 'Amores à Parte', 'nota': 7.1},
        {'classificação': '7', 'título': 'Uma Sexta-Feira Mais Louca Ainda', 'nota': 7.0},
        {'classificação': '8', 'título': 'Juntos', 'nota': 6.9},
        {'classificação': '9', 'título': 'Amores Materialistas', 'nota': 6.4},
        {'classificação': '10', 'título': 'Invocação do Mal 3', 'nota': 6.3}
    ]

    return render_template('ranking.html', lista_filmes = filmes)

if __name__ == '__main__':
    app.run(debug=True, port=5001)