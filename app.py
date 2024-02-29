import database
from flask import Flask, redirect, render_template, request, url_for
import datetime

app = Flask(__name__)
app.teardown_appcontext(database.close_db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create_article():
    return render_template('create.html')

@app.route('/register', methods=('GET', 'POST'))
def register_article():

    if 'user' not in request.form:
        er ="人物名が設定されていません"
        return render_template('create.html',er=er)
    else:
        user = request.form['user']

    if 'breastfeeding' not in request.form:
        breastfeeding = ""
    else:
        breastfeeding = request.form['breastfeeding']

    if 'urine' not in request.form:
        urine = ""
    else:
        urine = request.form['urine']

    if 'flight' not in request.form:
        flight = ""
    else:
        flight = request.form['flight']

    now = datetime.datetime.now()
    now = f'{now:%H:%M}'
    db = database.get_db()
    db.execute(
        "INSERT INTO POST (USER, URINE,FLIGHT,breastfeeding,now) VALUES ( ?,?, ?, ?,?)",
        (user, urine, flight, breastfeeding, now)
    )
    db.commit()
    return redirect(url_for('index'))

@app.route('/list')
def read_articles():
    db = database.get_db()
    articles = db.execute("SELECT * FROM POST")
    return render_template('list.html', articles=articles,)

@app.route('/delete/<int:id>')
def delete_article(id):
    db = database.get_db()
    db.execute("DELETE FROM POST WHERE ID=?", (id, ))
    db.commit()
    return redirect(url_for('read_articles'))

if __name__ == '__main__':
    app.run(debug=True)