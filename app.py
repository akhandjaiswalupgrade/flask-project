# app.py
from flask import Flask,request, jsonify
from flask.templating import render_template

from auth.routes import auth_bp #improt karne ke liye auth ke routes ka protocol
from users.routes  import userlogin
import database

app = Flask(__name__)



app.register_blueprint(auth_bp)

app.register_blueprint(userlogin)



@app.route('/')
def home():
    return render_template('home.html' , name="Akhand")

@app.route('/shop')
def products():
    return "Products are Listed Here "


@app.route('/future',  methods=['POST'])
def futuregenerate():
    day = request.form['DOB']
    name= request.form['name']
    return render_template ('future.html' , day = day, name=name)


@app.route('/api/data', methods=['POST'] )
def data():
    day = request.form['DOB']
    name= request.form['name']
    return jsonify({"Day of Birth": day, "Name": name})



if __name__ == '__main__':
    app.run(debug=True)
