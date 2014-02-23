
from bottle import route, run, template

index_html = '''My first web app! By {{ author }}'''



@route('/')
def index():
    return template(index_html, author='your name here')

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)


@route('/:anything')
def something(anything=''):
    return template(index_html, author=anything)

@route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)

@route('/show/<name:re:[a-z]+>')
def callback(name):
    assert name.isalpha()

if __name__ == '__main__':
    run(host='localhost', port=9000, debug=True, reload=True)