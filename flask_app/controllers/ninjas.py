from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def ninjas():
    dojos = Dojo.get_all()
    return render_template("ninjas.html", all_dojos = dojos)

@app.route("/add_ninja", methods=["POST"])
def add_ninjas():
    Ninja.save(request.form)
    return redirect("/dojos")
