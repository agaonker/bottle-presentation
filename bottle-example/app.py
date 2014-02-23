from bottle import route, request,response,\
 run, template, view, redirect
from bottle import Bottle

app = Bottle()

USER = "bottle"
PWD = "bottle"
SUPER_SECRET = "shhh secrete key"

def verify(user, pwd):
	if user == USER and pwd == PWD:
		return True
	else:
		return False

def isloggedin(callback):
    def wrapper(*args, **kwargs):
        username = request.get_cookie("account", secret=SUPER_SECRET)
        if username == USER:

            return callback(*args, **kwargs)
        redirect('/login')
    return wrapper

#bottle.install(isloggedin)

@app.route('/login')
def login():
    return '''
<form action="/home" method="post">
    Username: <input name="username" type="text" />
    Password: <input name="password" type="password" />
    <input value="Login" type="submit" />
</form>
    '''

@app.route('/home', method="POST")
@view('./views/home.tpl')
def home():
	username = request.forms.get('username')
	password = request.forms.get('password')
	if verify(username, password):
	    response.set_cookie("account", username, secret=SUPER_SECRET)
	    return dict(name=username)
	else:
	    return "<p>Login failed.</p>"


@app.route('/calculate', apply=[isloggedin])
def calculate():
    return "<b>You are in Authenticated page</b>"


@app.route('/logout', apply=[isloggedin])
def calculate():
    response.set_cookie("account", "")
    return "<b>You are logged out</b>"

run(app=app, host='localhost', port=9000, reloader=True)