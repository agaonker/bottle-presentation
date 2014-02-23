from bottle import response, install, route, run, redirect
import bottle
import time


def stopwatch(callback):
    def wrapper(*args, **kwargs):
        start = time.time()
        
        body = callback(*args, **kwargs)
        end = time.time()
        response.headers['X-Exec-Time'] = str(end - start)
        print str(callback)
        print str(end - start)
        redirect('/redirected/ashish')
        return body
    return wrapper

bottle.install(stopwatch)
s = stopwatch


@route('/hello/:name', apply=[s])
def index(name='World'):
    return '<b>Hello %s!</b>' % name

@route('/redirected/:name', apply=[])
def newindex(name='World'):
    return '<b>Hello Redirected %s!</b>' % name

run(host='localhost', port=8888)