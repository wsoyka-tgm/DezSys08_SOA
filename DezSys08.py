from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Possible improvements
# =====================
# Context menu for Edit, Delete
# Proper response (with status codes etc)
# Logging
# document code
# error handling (currently just showing e.g. notification: Internal server error)
# proper use of flask template
# etc

# Work done
# =========
# restful (all GET)
# restful proper way (GET PUT POST DELETE)
# db connection
# website
# jquery, bootstrap
# ui enhancements
# javascript methods
# notifications
# etc


def doquery(query):
    """
    Establishes a connection to a db and runs a query, the result of which is returned in a list (containing touples)
    :param query: a MySQL query
    :return: list with query result
    """
    con = pymysql.connect(host='10.0.0.17', port=3306, user='judith', passwd='judith', db='judith')
    cur = con.cursor()
    cur.execute(query)
    a = []
    for row in cur:
        a.append(row)
    con.commit()
    cur.close()
    con.close()
    return a


@app.route('/add/<name>/<text>', methods=['POST'])
def add(name, text):
    query = "INSERT INTO viki (name, text) VALUES ('%s', '%s');" % (name, text)
    doquery(query)
    return "added"


@app.route('/edit/<id>/<newname>/<newtext>', methods=['PUT'])
def edit(id, newname, newtext):
    query = "UPDATE viki SET name='%s', text='%s' WHERE id = %s;" % (newname, newtext, id)
    doquery(query)
    return "edited"


@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    query = "DELETE FROM viki WHERE id = %s;" % id
    doquery(query)
    return "deleted"


@app.route('/search/<tak>', methods=['GET'])
def search(tak):
    query = "SELECT v.id, v.name, v.text FROM viki v JOIN tak t WHERE v.id = t.viki_id AND t.name LIKE '%%%s%%' OR v.name LIKE '%%%s%%' GROUP BY v.id;" % (
    tak, tak)
    asd = doquery(query)
    out = "["
    for x in asd:
        ex = '{"id":%s, "name": "%s", "text":"%s"},' % (x[0], x[1], x[2])
        out += ex
    out = out[:-1]  # remove last comma
    out = out + "]"
    return out


@app.route('/')
@app.route('/index')
@app.route('/crud')
def crud():
    return render_template('template.html', site="crud.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
