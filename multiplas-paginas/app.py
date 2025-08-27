from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/ingressos')
def ingressos():
    return render_template('ingressos.html')

@app.route('/cinemas')
def cinemas():
    return render_template('cinemas.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)