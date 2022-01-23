from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)


@app.route('/create_dojo',methods=['POST'])
def create_dojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.save(request.form) # submit form directly in as data if formated same as dictionary
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojos.html')