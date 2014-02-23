from bottle import Bottle, route, run, template, error
from bottle import static_file, get, post, request


app = Bottle()

index_str = "Hello GNUnify from : {{name}}"

@app.route("/")
@app.route("/hello/:name")
def index(name="Stranger"):
	return template(index_str, name=name.title())

@app.route('/object/<num:int>')
def callback(num):
    assert isinstance(num, int)
    return "Its is integer : %d"%num

@app.route('/object')
def object_fn():
	return "hello"


@app.route('/object/<string:re:[a-z0-9]+>')
def callback(string):

    return "Regex Match for : %s"%string

@app.route('/static/<filename:re:.*\.jpeg>')
def send_image(filename):
    return static_file(filename, root='./static', mimetype='image/jpeg')

@app.route('/download/<filename:path>')
def down_image(filename):
    return static_file(filename, root='./static', download=filename)

@app.error(404)
def error404(error):
    return 'Nothing here, sorry'

@app.error(500)
def error500(error):
	return "Some Error on server. check logs on console"

@app.get('/where')
def location():
	return """<h1>Where are you? </h1>
	<form method="POST", action="where">
		Enter Location <input type="text" name="loc"/>
	</form>"""

@app.post('/where')
def gotit():
	loc = request.forms.get('loc')
	return "<h1>Location is : %s</h1>"%loc

run(app=app, host="localhost", port=9000, reloader=True)
 	