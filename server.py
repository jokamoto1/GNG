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
    session['name'] = f"<h3> Name: <span class='text-warning'>  {request.form['name']} </span> </h3>"
    session['location'] = f"<h3> Location: {request.form['location']} </h3>"
    session['language'] = f"<h3> Language: {request.form['language']} </h3>"
    session['comments'] = f"<h3> Comments: {request.form['comments']} </h3>"
    return redirect("result")

@app.route("/result")
def show_user():
    print(session['name'])
    print(session['location'])
    print(session['language'])
    print(session['comments'])
    return render_template('index2.html')
@app.route("/destroy")
def destroy():
    del session['name']
    del session['location']
    del session['language']
    del session['comments']
    return redirect('/')
if __name__ == "__main__":
        app.run(debug=True)   