from flask import render_template, flash, redirect, session
from flask_app import app

@app.route('/')
def inicio():
    return render_template('portada.html')

@app.route('/panel')
def panel():
    if 'usuario' not in session:
        flash("no estás logeado!!!!", "error")
        return redirect("/login")


    return render_template(
        'inicio.html',
    )