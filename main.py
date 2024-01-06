import flask

app = flask.Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    nomes = ['auridebson', 'luciana', 'levy', 'guilherme', 'angelina', 'thobias', 'zoe']
    return flask.render_template('index.html',nomes=nomes)

@app.route('/about')
def about():
    return "<h1>Página Sobre</h1>"

if __name__ == '__main__':
    app.run(debug=True) 

