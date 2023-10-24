import flask

app = flask.Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

@app.route('/about')
def about():
    return "<h1>Página Sobre</h1>"

if __name__ == '__main__':
    app.run(debug=True)
