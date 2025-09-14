from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "omaein_compra_boobiesgoddies"

users = [
    {"name": "Levi", "email": "levi@gmail.com", "password": "123"}
]

@app.route('/')
def pagina_csr():
    return render_template('csr.html')

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
                return redirect(url_for('pagina_csr'))
        
        return render_template('login.html', erro="Username, email ou senha incorretos")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Você foi desconectado com sucesso!", "sucesso")
    return redirect(url_for('pagina_csr'))

if __name__ == '__main__':
    app.run(debug=True)
