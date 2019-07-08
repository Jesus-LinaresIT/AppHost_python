from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

dbDir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbDir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	titleD = db.Column(db.String(30))		

@app.route("/filePython/<string:project>/<string:user>")
def userA(project = "Project", user = "Linares"):
	title = "Welcome!!"
	lis = []
	return render_template("Index.html", title=title, lis=lis)

@app.route("/insert/inquilino") 
def insert_inquilino():
	#new_post = Posts(titleD = "Resident sick")
	#db.session.add(new_post)
	#db.session.commit()
	inquilino_Created = "The new inquilino was created"

	return render_template("insert_inquilino.html", inquilino = inquilino_Created)
 
@app.route("/select/inquilino") 
def queryId_inquilino():
	post = Posts.query.filter_by(id = 4).first()
	queryR = "The result of the Query is: ", post.titleD

	return render_template("findInquilinos.html", queryR = queryR)

if __name__ == "__main__":
	db.create_all()
	app.run(debug = True, host ='0.0.0.0', port = 8090)