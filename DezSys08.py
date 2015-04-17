from flask import Flask, render_template, jsonify
import pymysql

app = Flask(__name__)


def doquery(query):
    conn = pymysql.connect(host='10.0.106.113', port=3306, user='judith', passwd='judith', db='judith')
    cur = conn.cursor()
    cur.execute(query)
    #print(cur.description)
    a = []
    for row in cur:
        a.append(row)
    conn.commit()
    cur.close()
    conn.close()
    return a


@app.route('/add/<name>/<text>')
def add(name, text):
    query = "INSERT INTO viki (name, text) VALUES ('%s', '%s');" % (name, text)
    return jsonify(doquery(query))



@app.route('/edit/<id>/<newname>/<newtext>')
def edit(id, newname, newtext):
    query = "UPDATE viki SET name='%s', text='%s' WHERE id = %s;" % (newname, newtext, id)
    return jsonify(doquery(query))


@app.route('/delete/<id>')
def delete(id):
    query = "DELETE FROM viki WHERE id = %s;" % (id)
    print(query)
    return jsonify(doquery(query))

@app.route('/search/<tak>')
def search(tak):
    query = "SELECT v.id, v.name, v.text FROM viki v JOIN tak t WHERE v.id = t.viki_id AND t.name LIKE '%%%s%%' OR v.name LIKE '%%%s%%' GROUP BY v.id;" % (tak, tak)
    asd = doquery(query)
    out = "["
    for x in asd:
        ex = '{"id":%s, "name": "%s", "text":"%s"},' % (x[0], x[1], x[2])
        out += ex
    out = out[:-1] # remove last comma
    out = out + "]"
    return out


@app.route('/judith')
def judith():
    return '"Soa is ur toll und macht mega viel spaß." </br><div style="padding:left">- Judith</div>'

@app.route('/')
@app.route('/index')
@app.route('/crud')
def crud():
    return render_template('template.html', site="crud.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
