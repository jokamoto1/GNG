from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'adfasfdsafsdfas'

@app.route('/')
def index():
    if 'name' not in session:
        session['name'] = ''
    if 'location' not in session:
        session['location'] = ''
    if 'language' not in session:
        session['language'] = ''
    if 'comments' not in session:
        session['comments'] = ''
    return render_template('index.html')

@app.route("/create_user", methods=['POST'])  
def create_user():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect("result")

@app.route("/result")
def show_user():
    return render_template('index.html-2')

if __name__ == "__main__":
        app.run(debug=True)   