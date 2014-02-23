from bottle import run, template, get, post, request, error,view

@get('/plot')
def form():
    return '''
              <form method="POST" action="/plot">
                Name: <input name="name" type="text" />
                Age: <input name="age" type="text" /><br/>              
                <input type="submit" />
              </form>'''

@post('/plot')
@view('views/simple.tpl')
def submit():
    name   = request.forms.get('name')
    age    = request.forms.get('age')
    return dict(name=name, age=age)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

if __name__ == '__main__':

    run(host='localhost', port=9000, debug=True)