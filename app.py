from bottle import route, run
from datetime import datetime

@route('/')
def hello():
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f'''
    <h1>HELLO WORLD</h1>
    <p>#PBW3B1PBL0101</p>
    <p>251080200077</p>
    <p>NAYLA_RAHMA_ALMUMIN</p>
    <p>Framework Pilihan → Python [7] - Bottle</p>
    <p>TIME : {waktu}</p>
    '''

run(host='localhost', port=8080, debug=True)
