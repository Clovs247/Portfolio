from flask import render_template, redirect, session, flash
from flask_app import app



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")


