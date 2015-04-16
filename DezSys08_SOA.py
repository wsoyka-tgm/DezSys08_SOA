from flask import Flask, render_template, jsonify
import pymysql

app = Flask(__name__)


def doquery(query):
    conn = pymysql.connect(host='10.0.0.29', port=3306, user='judith', passwd='judith', db='judith')
    cur = conn.cursor()
    cur.execute(query)
    print(cur.description)
    print("--------")
    print(cur)
    a = []
    for row in cur:
        print(row)
        a.append(row)

    cur.close()
    conn.close()
    return a


@app.route('/add/<name>/<text>')
def add(name, text):
    query = "INSERT INTO viki (name, text) VALUES ('%s', '%s');" % (name, text)
    return jsonify(doquery(query))



@app.route('/edit/<name>')
def edit(name):
    return 'Edit'


@app.route('/delete/<name>')
def delete(name):
    query = "DELTE FROM viki WHERE name = '%s';" % (name)
    doquery(query)

@app.route('/search/<tak>')
def search(tak):
    query = "SELECT v.name, v.text FROM viki v JOIN tak t WHERE v.id = t.viki_id AND t.name LIKE '%s';" % (tak)
    print(doquery(query))
    return "asdasdasds"


@app.route('/judith')
def judith():
    return '"DezSys08_SOA i s ur toll und macht mega viel spaß." </br><div style="padding:left">- Judith</div>'


@app.route('/crud')
def crud():
    return render_template('template.html', site="crud.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

