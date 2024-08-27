from flask import Flask
from flask import request,redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    print("Witaj na stronie mojej wizytowki")
    return render_template('wizytowka.html')

@app.route('/kontakt', methods=['GET','POST'])
def kontakt():
    if request.method == 'GET':
        print("We have GET in da house")
        return render_template("kontakt.html")
    elif request.method == 'POST':
        print("POST POST POST")
        x = request.form
        for i in x.values():
            print(f'wartosc wpisana w formularz: {i}')
        return redirect('/')