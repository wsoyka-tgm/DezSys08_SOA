from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'DezSys08_SOA is ur toll und macht mega viel spaß.'


if __name__ == '__main__':
    app.run()
