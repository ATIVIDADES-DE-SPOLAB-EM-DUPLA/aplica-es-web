from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina_csr():
    return render_template('csr.html')

if __name__ == '__main__':
    app.run(debug=True)