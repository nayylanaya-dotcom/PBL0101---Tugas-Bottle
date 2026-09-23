from bottle import route, run

@route('/')
def hello():
    return 'HELLO WORLD'

run(host='localhost', port=8080, debug=True)