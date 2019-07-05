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
	title = "Function all"
	lis = ["Inicio", "News", "Contacts"]
	return render_template("Index.html", title=title, lis=lis)

@app.route("/insert/resident") #Interactuar con el template para mostrar datos en html
def insert_default():
	#new_post = Posts(titleD = "Resident Evil")
	#db.session.add(new_post)
	#db.session.commit()

	return render_template("select.html")

	#return "the resident Evil was created" 

@app.route("/select/default") #Interactuar con el template para mostrar favicon
def select_default():
	post = Posts.query.filter_by(id = 4).first()

	return f"the result of the Query is: {post.titleD}"

	return render_template("query_select.html")

if __name__ == "__main__":
	db.create_all()
	app.run(debug = True, host ='0.0.0.0', port = 8090)