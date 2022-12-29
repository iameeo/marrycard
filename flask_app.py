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

@app.route('/emp02')
def emp():
    empList = MyEmpDao().getEmps();
    return render_template("emp02.html", empList=empList)

@app.route('/article/<int:articleID>/')
def board_content(articleID):
    article = MyEmpDao().testEmps(articleID);
    return render_template('/article.html', article=article)

@app.route('/ins.ajax', methods=['POST'])
def ins_ajax():
    data = request.get_json()
    empno = data['empno']
    name = data['name']
    department = data['department']
    phone = data['phone']
    cnt = MyEmpDao().insEmp(empno, name, department, phone)
    result = "success" if cnt==1 else "fail"
    return jsonify(result = result)
 
@app.route('/mod.ajax', methods=['POST'])
def mod_ajax():
    data = request.get_json()
    empno = data['empno']
    name = data['name']
    department = data['department']
    phone = data['phone']
    cnt = MyEmpDao().updEmp(empno, name, department, phone)
    result = "success" if cnt==1 else "fail"
    return jsonify(result = result)
 
@app.route('/del.ajax', methods=['POST'])
def del_ajax():
    data = request.get_json()
    empno = data['empno']
    cnt = MyEmpDao().delEmp(empno)
    result = "success" if cnt==1 else "fail"
    return jsonify(result = result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
