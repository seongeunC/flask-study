#Flask module import
from flask import Flask
#redirect , url_for module import
from flask import redirect,url_for
#request
from flask import request
#render_template
from flask import render_template

#Flask의 생성자는 current module(__name__)을 인자로 받음
app = Flask(__name__)

#1 번째 방법
#app.route(rule,options)  rule: 함수와 연결된 URL  , options: rule객체에 전달될 인자 목록
@app.route('/')
def hello_world():
    return 'hello world'

#2 번째 방법
#routing 기능 add_url_rule()함수
def hello_world2():
    return 'hello world2'
app.add_url_rule('/hello','hello_world2',hello_world2)

#3 번째 방법
#url 변수활용(symentic URL(?))
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' %name

#4 번째 방법
#url 변수활용 - 자료형 변환
@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Post Number %d' %postID

#5 번째 방법
#redirect
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' %guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

#6 번째 방법
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET']) 
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

#7 번째 방법(url 변수) - hello.html
@app.route('/show/<user>')
def show(user):
    return render_template('hello.html',name = user)

#8 번째 방법   - show2.html
@app.route('/show2/<int:score>')
def show2(score):
    return render_template('show2.html',marks=score)

#9 번째 방법 - dic 파일 출력 (json 형태 표로 출력하는 방법(?))  -result.html
@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

#10 번째 방법 - static파일(js function)을 불러드림 - static.html
@app.route('/static_file')
def static_file():
    return render_template("static.html")

#11 번째 방법 - data 입력 후 url 이동 후 출력 - student.html / student_result.html
@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/student/result', methods = ['POST','GET'])
def student_result():
    if request.method =='POST':
        result = request.form
        return render_template("student_result.html",result=result)

if __name__ == '__main__':
    #코드가 수정될 때 마다 스스로 수정 재시작
    #애플리케이션에 발생할 수 있는 에러 추적 가능
    app.debug = True
#flask의 run()은 로컬 개발 서버에 애플리케이션 실행
#app.run(host,port,debug,options) 모든 인자는 선택적.
#host :응답을 받는 hostname ('127.0.0.1'이 기본값, 외부 사용가능 서버'0.0.0.0')
#port :기본값 5000
#debug : 기본값 false,만약 true면 debug정보 제공
#options : Werkzeug 서버에 전달할 내용
    app.run('localhost',3000)
