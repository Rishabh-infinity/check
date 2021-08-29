from flask import Flask, render_template, url_for, request
from database import db_session
from models import User

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user_form", methods=["POST", "GET"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    else:
        data = request.form
        data_tuple = tuple(data.values())
        print(data_tuple)
        user = User(data_tuple[0], data_tuple[1], data_tuple[2])
        db_session.add(user)
        db_session.commit()
        print("data is entered into database!")
        return render_template("registered.html", data=data)

@app.route("/all_users")
def all_users():
    users = User.query.all()
    return render_template("all_users.html", users = users)

if __name__ == "__main__":
    app.run(debug=True)