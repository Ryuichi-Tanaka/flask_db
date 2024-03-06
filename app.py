import database
from flask import Flask, redirect, render_template, request, url_for
import datetime
import csv
from flask import send_file

app = Flask(__name__)
app.teardown_appcontext(database.close_db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create_article():
    return render_template('create.html')


@app.route('/download')
def download():
    return send_file("src/result.csv",
mimetype="text/csv",
as_attachment=True,)

@app.route('/download1')
def download1():
    return send_file("src/result2.csv",
mimetype="text/csv",
as_attachment=True,)


@app.route('/create2')
def create2():
    return render_template('create2.html')

@app.route('/register', methods=('GET', 'POST'))
def register_article():

    if 'user' not in request.form:
        er ="人物が設定されていません"
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

    if 'bikou' not in request.form:
        bikou = ""
    else:
        bikou = request.form['bikou']

    now = datetime.datetime.now()
    now = f'{now:%H:%M}'
    db = database.get_db()
    db.execute(
        "INSERT INTO POST (USER, URINE,FLIGHT,breastfeeding,now,bikou) VALUES ( ?,?, ?, ?,?,?)",
        (user, urine, flight, breastfeeding, now,bikou)
    )
    db.commit()
    db = database.get_db()
    articles = db.execute("SELECT * FROM POST")
    return render_template('list.html',articles=articles)



""" @app.route('/register1', methods=('GET', 'POST'))
def totals():

    if 'light' not in request.form:
        er ="体温：右が設定されていません"
        return render_template('create2.html',er=er)
    else:
        light = request.form['light']

    if 'left' not in request.form:
        er ="体温：左が設定されていません"
        return render_template('create2.html',er=er)
    else:
        left = request.form['left']
    now = datetime.datetime.now()
    now = f'{now:%H:%M}'
    db = database.get_db()
    db.execute(
        "INSERT INTO TENPRERATURE (now,LIGHT,LEFT) VALUES ( ?,?, ?)",
        (now,light,left)
    )
    db.commit()
    db = database.get_db()
    totals = db.execute("SELECT * FROM TENPRERATURE")
    return render_template('list2.html',totals=totals) """



@app.route('/list')
def read_articles():
    db = database.get_db()
    articles = db.execute("SELECT * FROM POST order by date desc")
    return render_template('list.html', articles=articles)

""" @app.route('/list2')
def read_tenprerature():
    db = database.get_db()
    totals = db.execute("SELECT * FROM TENPRERATURE")
    return render_template('list2.html', totals=totals) """

@app.route('/delete/<int:id>')
def delete_article(id):
    db = database.get_db()
    db.execute("DELETE FROM POST WHERE ID=?", (id, ))
    db.commit()
    return redirect(url_for('read_articles'))

@app.route('/delete/<int:id>')
def delete_total(id):
    db = database.get_db()
    db.execute("DELETE FROM TENPRERATURE WHERE ID=?", (id, ))
    db.commit()
    return redirect(url_for('read_tenprerature'))

@app.route('/result')
def create_csv():
    db = database.get_db()
    rows = db.execute("SELECT * FROM POST").fetchall()
    with open("src/result.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            f.truncate(0)
            writer.writerow(["ひづけ","じかん","きろくしたひと","みるく","おしっこ","うんち" ])
            for row in rows:
                writer.writerow([row['DATE'],row['now'],row['USER'], row['breastfeeding'], row['urine'], row['flight']])
            return render_template('result.html')
    
""" @app.route('/result2')
def create_csv2():
    db = database.get_db()
    rows = db.execute("SELECT * FROM TENPRERATURE").fetchall()
    with open("src/result2.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            f.truncate(0)
            writer.writerow(["日付","時間","体温：左","体温：右"])
            for row in rows:
                writer.writerow([row['DATE'],row['now'],row['LEFT'], row['LIGHT']])
            return render_template('result2.html') """


@app.route('/find')
def find():
    text_input = request.args.get('search')
    db = database.get_db()
    finds = db.execute("SELECT * FROM POST WHERE user LIKE ? OR date LIKE ? OR now LIKE ? OR breastfeeding LIKE ? OR urine LIKE ? OR flight LIKE ? OR bikou LIKE ?", ('%' + text_input + '%', '%' + text_input + '%', '%' + text_input + '%','%' + text_input + '%', '%' + text_input + '%', '%' + text_input + '%','%' + text_input + '%'))
    return render_template('list.html',finds=finds)

if __name__ == '__main__':
    app.run(debug=True)


