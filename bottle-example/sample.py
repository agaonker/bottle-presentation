from bottle import route, run, Bottle, template, view
from bottle import get, post, request, error
app = Bottle()

tpl_str = "hello {{ name }}"

@app.route('/hello')
@app.route('/hello/<name>')
def index(name="Guest"):
	return "hello, Welcome :%s"%name

@app.route('/test/<num:re:[a-z0-9]+>')
def test(num):
	return "Its an int : %s"%num

@app.route('/template/<name>')
@view('./views/basic.tpl')
def tpl(name):
	return dict(name=name)

@app.get('/login')
@view('./login.tpl')
def login():
	return dict()

@app.post('/login')
def post_login():
	name = request.forms.get('user')
	return "user name : %s"%name

@app.error(404)
def handle404(error):
	return "Nothing here"







run(app=app, host="localhost", port=9000,debug=True, reloader=True)
