#imports from flask framework
from flask import Flask, Response, render_template, request, session, make_response, send_file
from werkzeug.utils import secure_filename
#imports from flask plugins
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#imports from site packages
import click
#imports from standart library
import os
import json
import secrets

#constants
UPLOAD_FOLDER = "/user_files"
ALLOWED_EXTENSIONS = ["stl", "3mf", "obj", "prt", "dwg", "pdf", "dxf"]

#function for securing uploaded files filenames
def is_allowed(filename):
    return "." in filename and filename.split(".")[1].lower() in ALLOWED_EXTENSIONS

#creating flask application
app = Flask(__name__,
            static_folder = "../dist/assets",
            template_folder = "../dist")

#setting sqlite database filename
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

#Flask secret key for  interacting with sessions
app.secret_key = secrets.token_urlsafe(16)

#setting app database and encryption plugins
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#creating database tables for questions and for admins
class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    question = db.Column(db.Text, nullable=False)
    user_file = db.Column(db.String(100), nullable=True, unique=True)

    def __repr__(self):
        return("email: {0}, question: {1}, file: {2}".format(self.email, self.question, self.user_file))

    def to_dict(self):
        return ({
            "email": self.email,
            "question": self.question,
            "file": self.user_file,
            "id": self.id
        })

class Admins(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)

#Setting up routes
@app.route('/question/', methods=["POST"])
def get_question():
    email = request.form["email"]
    text = request.form["question"]
    if request.files:
        user_file = request.files['file']
        filename_key = secrets.token_hex(4)
        filename = filename_key + secure_filename(user_file.filename)
        user_file.save(os.path.join(app.root_path, 'user_files/{}'.format(filename)))
        question = Questions(email=email, question=text, user_file=filename)
    else:
        question = Questions(email=email, question=text)
    db.session.add(question)
    db.session.commit()
    res = Response()
    res.status_code = 201
    return res

@app.route('/question/', methods=["GET"])
def return_questions():
    res = Response()
    if session.get("is_admin") == True:
        res.status_code = 200
        data = json.dumps([item.to_dict() for item in Questions.query.all()])
        res.data = data
    else:
        res.status_code = 401
    return res


@app.route('/question/<int:id>', methods=['DELETE'])
def delete_question(id):
    question = Questions.query.filter_by(id=id).first()
    filename = question.user_file
    if filename:
        filepath = os.path.join(app.root_path, 'user_files/{}'.format(filename))
        if os.path.exists(filepath):
            os.remove(filepath)
        else:
            print("file not exist")
    db.session.delete(question)
    db.session.commit()
    res = Response()
    res.status_code = 200
    return res

@app.route('/question/file/<int:id>')
def send_user_file(id):
    filename = Questions.query.filter_by(id=id).first().user_file
    return send_file("user_files/{}".format(filename), attachment_filename=filename, as_attachment=True)


@app.route("/login/", methods=["POST"])
def login():
    form_data = request.form
    res = Response()
    admin = Admins.query.first()
    login = form_data["login"]
    password = form_data["password"]
    if login == admin.login and bcrypt.check_password_hash(admin.password, password):
        session["is_admin"] = True
        res.status_code = 200
    else:
        res.status_code = 401
        res.data = {"message": "wrong login or password"}
    return res

@app.route("/logout/", methods=["GET"])
def logout():
    res = Response()
    if (session.get("is_admin")):
        session["is_admin"] = False
        res.status_code = 200
    else:
        res.status_code = 500
        print("something wrong")
    return res

@app.route("/authasadmin/", methods=["GET"])
def admin():
    res = Response()
    if session.get("is_admin") == True:
        res.status_code = 200
    else:
        res.status_code = 401
    return res

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

@click.group()
def start():
    pass

@start.command(help="start server in debug mode")
def run_debug():
    app.run(debug=True)

@start.command(help="create admin account")
@click.option("--login", "-l", help="admin login")
@click.password_option()
def create_admin(login, password):
    print(login, password)
    pw_hash = bcrypt.generate_password_hash(password).decode()
    admin = Admins(login=login, password=pw_hash)
    db.session.add(admin)
    db.session.commit()
    print(bcrypt.check_password_hash(pw_hash, password))

@start.command(help="drop database")
def drop_database():
    db.drop_all()
    db.create_all()

@start.command()
def test_login():
    admin = Admins.query.first()
    print(admin.login, admin.password)

if __name__ == '__main__':
    start()