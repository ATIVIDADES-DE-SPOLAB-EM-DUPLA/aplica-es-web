from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mostrar_filmes():
    filmes = [
        {'título': 'Invocação do Mal', 'nota': 7.5},
        {'título': 'Invocação do Mal 2', 'nota': 7.3},
        {'título': 'Faça Ela Voltar', 'nota': 7.2},
        {'título': 'A Hora do Mal', 'nota': 7.1},
        {'título': 'Os Carasm Malvados 2', 'nota': 7.1},
        {'título': 'Amores à Parte', 'nota': 7.1},
        {'título': 'Uma Sexta-Feira Mais Louca Ainda', 'nota': 7.0},
        {'título': 'Juntos', 'nota': 6.9},
        {'título': 'Amores Materialistas', 'nota': 6.4},
        {'título': 'Invocação do Mal 3', 'nota': 6.3}
    ]

    return render_template('ranking.html', lista_filmes = filmes)

if __name__ == '__main__':
    app.run(debug=True)

#from flask import Flask, render_template
#app = Flask(__name__)
#@app.route('/notas')
#def mostrar_notas():
# alunos = [
# {'nome': 'Ana', 'nota': 9.5},
# {'nome': 'Beto', 'nota': 6.0},
# {'nome': 'Carlos', 'nota': 4.5}
# ]
#
# return render_template('notas.html', lista_de_alunos=alunos)
#if __name__ == '__main__':
# app.run(debug=True, port=5001)