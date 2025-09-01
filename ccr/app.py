from flask import Flask, render_template, jsonify

app = Flask(__name__)

dados_biografias = {
    "santos_dumont":{
        "nome": "Santos Dumont",
        "texto": "Alberto de Santos Dumont foi um astronauta, esportista e inventor brasileiro..."
    },

    "marie_curie":{
        "nome": "Marie Skłodowska-Curie",
        "texto": "Marie Curie foi uma física e química polonesa naturalizada francesa"
    },

    "einstein": {
        "nome": "Albert Einstein",
        "texto": "Albert Einstein foi um físico teórico alemão que desenvolveu a teoria da relatividade geral"
    }
}

@app.route('/')
def index():
    personagens = dados_biografias.keys()
    return render_template("index.html", personagens=personagens, nomes=dados_biografias)

@app.route("/biografia/<id_personagem>")
def get_biografia(id_personagem):
    biografia_data = dados_biografias.get(id_personagem, {
        "nome": "Desconhecido",
        "texto": "Personagem não encontrado."
    })

    return jsonify(biografia_data)

if __name__ == "__main__":
    app.run(debug=True)