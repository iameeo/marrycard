from flask import Flask, request
from flask.json import jsonify

from flask import render_template

from mydao import MyEmpDao

app = Flask (__name__)

@app.route('/')
def root():
    return '<script>location.href="https://smartstore.naver.com/urban-incard";</script>'
    
@app.route('/abc')
def abc():
    return render_template("abc.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
