from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "omaein_compra_boobiesgoddies"

users = [
    {"name": "Levi", "email": "levi@gmail.com", "password": "123"}
]

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

    logado = session.get('logado', False)
    usuario = session.get('user_name')
    
    return render_template('ranking.html', lista_filmes=filmes, logado=logado, usuario=usuario)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        username = request.form['username']
        useremail = request.form['email']
        userpassword = request.form['password']        
        
        for user in users:
            if user['email'] == useremail:
                return render_template('cadastro.html', erro="Email já cadastrado")
        
        new_user = {
            "name": username,
            "email": useremail,
            "password": userpassword
        }
        users.append(new_user)
        
        flash("Cadastro realizado com sucesso! Faça login para continuar.", "sucesso")
        return redirect(url_for('validar_login'))
    
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def validar_login():
    if request.method == "POST":
        username = request.form['username']
        useremail = request.form['email']
        userpassword = request.form['password']

        for user in users:
            if (user['email'] == useremail) and (user['password'] == userpassword) and (user.get('name') == username):
                session['logado'] = True
                session['user_email'] = useremail
                session['user_name'] = user['name']
                flash("Login realizado com sucesso!", "sucesso")
                return redirect(url_for('mostrar_filmes'))
        
        return render_template('login.html', erro="Username, email ou senha incorretos")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Você foi desconectado com sucesso!", "sucesso")
    return redirect(url_for('mostrar_filmes'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)