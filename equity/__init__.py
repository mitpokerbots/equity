import os
from flask import Flask, request, render_template
from flask_sslify import SSLify

from pbots_calc import calc

app = Flask(__name__)
config_object_str = 'equity.config.ProdConfig' if os.environ.get('PRODUCTION', False) else 'equity.config.DevConfig'
app.config.from_object(config_object_str)

def get_cards(s, all=False):
    if s.strip() == '' and all:
        return 'xx'
    return s.strip()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        board = get_cards(request.form['board'])
        hole = get_cards(request.form['hole'], all=True)
        opponent = get_cards(request.form['opponent'], all=True)
        discard = get_cards(request.form['discard'])

        result = calc(hole + ":" + opponent, board, discard, 100000)

        if result is None:
            return render_template('index.html', result='fail', hole=hole, opponent=opponent, board=board, discard=discard)

        return render_template('index.html', result='success', evs=result.ev, hole=hole, opponent=opponent, board=board, discard=discard)
