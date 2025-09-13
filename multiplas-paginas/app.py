from flask import Flask, render_template, request, redirect, url_for, make_response, session

app = Flask(__name__)

app.secret_key = 'ChaveSupersecreta'

users = [
    {'email': 'levi@gmail.com', 'password': '123', 'name': 'levi'}
]
@app.route('/')
def pagina_inicial():
    return render_template('index.html', logado=session.get('logado', False), usuario=session.get('user_name', None))

@app.route('/ingressos')
def ingressos():
    return render_template('ingressos.html', logado=session.get('logado', False), usuario=session.get('user_name', None))

@app.route('/cinemas')
def cinemas():
    return render_template('cinemas.html', logado=session.get('logado', False), usuario=session.get('user_name', None))

@app.route('/noticias')
def noticias():
    return render_template('noticias.html', logado=session.get('logado', False), usuario=session.get('user_name', None))

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
                return redirect(url_for('pagina_inicial'))
            
        return render_template('login.html', erro="Username, email ou senha incorretos")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('pagina_inicial'))

if __name__ == '__main__':
    app.run(debug=True)