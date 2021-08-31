import sqlite3

from flask import Flask, render_template, url_for, request, make_response, session, redirect
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "any random string"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        return render_template("index.html", isLogin=True)
    return render_template("plzLogin.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            session['username'] = request.form['username']
            with sqlite3.connect('database.db') as con:
                print("----")
                cursor = con.cursor()
                query = 'INSERT INTO user (name) VALUES ("{}")'.format(username)
                print(query)
                cursor.execute(query)
                con.commit()
                print("added to database")
                return redirect(url_for('index', isLogin=True))
        except:
            print("HERE")
            con.rollback()
            return redirect(url_for("index", isLogin=False))
    else:
        return render_template("login.html")
    con.close()

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route("/user_form", methods=["POST", "GET"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    else:
        return render_template("registered.html", data=request.form)



@app.route("/setcookie", methods=["POST", "GET"])
def setcookie():
    if request.method == "POST":
        name = request.form['username']
        email = request.form['email']
        resp = make_response(render_template("registered.html",data=request.form))
        resp.set_cookie('username', name)
        resp.set_cookie('email', email)
        return resp



@app.route("/user_cookie")
def user_cookie():
    name = request.cookies.get('username')
    email = request.cookies.get('email')
    return "<h1>Name: {}</h1> <br> <h2>Email: {}</h2>".format(name, email)

if __name__ == "__main__":
    app.run(debug=True)