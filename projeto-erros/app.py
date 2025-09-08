from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/area-restrita')
def area_restrita():
    print("Tentativa de acessoa à área restrita sem autenticação")
    abort(401)

@app.errorhandler(401)

@app.route('/painel-admin')
def painel_admin():
    print("Tentativa de acesso ao painel do admin sem permissão")
    abort(403)

@app.errorhandler(403)

def pagina_nao_encontrada(error):
    return render_template('404.html'), 404

@app.errorhandler(401)

def nao_autorizado(error):
    return render_template('401.html'), 401

@app.errorhandler(403)

def acesso_proibido(error):
    return render_template('403.html'), 403

if __name__ == '__main__':
    app.run(debug=True)