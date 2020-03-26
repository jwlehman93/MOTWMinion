#test="jay"
#print(f"Hello World. {test} has and always will be the worst Reichart")

from flask import Flask, render_template
from ccform import ccform

import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def character_creation():
    form = ccform()
    return render_template('ccform.html', title='Hunter Formulation', form=form)

@app.route('/jay')
def fuq_jay():
    test = 'Jay'
    return 'Hello World. Jay has and always will be the BLACK sheep'





if __name__ == '__main__':
    app.run()
