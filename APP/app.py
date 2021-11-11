import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.Response('Site - Teste OK!')

if __name__ == '__main__':
    app.run() 
