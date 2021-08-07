from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'adfasfdsafsdfas'

@app.route('/')
def index():
    if 'guessNum' not in session:
        session['guessNum'] = random.randint(1,100)
    print(session['guessNum'])  
    return render_template('index.html')
    

@app.route('/guess', methods=['POST'])
def guess():
    try:
        session['userNum'] = int(request.form['userNum'])
        if session['guessNum'] == session['userNum']:
            session['msg'] = f"<div>CORRECT! </div>"            
        elif session['guessNum'] > session['userNum']:
            session['msg'] = f"<div>TOO LOW! </div>"
        elif session['guessNum'] < session['userNum']:
            session['msg'] = f"<div>TOO HIGH! </div>"
    except Exception:
        session['msg'] = "ERROR!"
    return redirect('/')
@app.route('/destroy')
def destroy():
    session['msg'] = f"<div>NUMBER AS BEEN RESET! </div>"
    del session['guessNum']
    return redirect('/')
if __name__ == "__main__":
        app.run(debug=True)   