from flask import Flask, render_template

app = Flask(__name__)
NOME_SITE = "India Eventos"  # Nome centralizado

@app.route('/')
def index():
    return render_template('index.html', nome_site=NOME_SITE)

@app.route('/perfil/<nome>')
def perfil(nome):
    return render_template('perfil.html', nome=nome, nome_site=NOME_SITE)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', nome_site=NOME_SITE)

@app.route('/contato')
def contato():
    responsavel = "João Silva"
    return render_template('contato.html', responsavel=responsavel, nome_site=NOME_SITE)

if __name__ == '__main__':
    app.run(debug=True)
