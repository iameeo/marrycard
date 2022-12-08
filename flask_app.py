from flask import Flask
from flask import render_template
app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!1234'
    
@app.route('/abc')
def abc():
    return render_template("abc.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
