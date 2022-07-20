from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.String(100))
    bday = db.Column (db.DateTime)

    def __init__(self, name, bday, license):
        self.name = name
        self.bday = bday
        self.license = license



@app.route('/')
def Index():
    return render_template("index.html")

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['Name']
        bday = request.form['D.O.B']
        license = request.form['License']

        my_data = Data(name, bday, license)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('Index'))



if __name__ == '__main__':
    app.run(debug=True)