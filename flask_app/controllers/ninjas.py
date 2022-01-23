from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import ninja, dojo

@app.route("/ninjas")
def ninjas():
    dojos = dojo.Dojo.get_all()
    return render_template("ninjas.html", all_dojos = dojos)

@app.route("/add_ninjas", methods=["POST"])
def add_ninjas():
    ninja.Ninja.save(request.form)
    return redirect("/")
