from flask import Flask
from flask import render_template
from nanpy import Arduino as A
import os
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')

app = Flask(__name__, template_folder=tmpl_dir, static_url_path='')
import datetime

red = 8
green = 11
A.pinMode(red, A.OUTPUT)
A.pinMode(green, A.OUTPUT)

@app.route("/")
def index():
	print 'TEMPLATE DIRECTORY'
	print tmpl_dir
	print 'Index Endpoint'
	templateData = {}
	return render_template('main.html', **templateData)

@app.route("/red")
def blinkRed():
    for ii in range(0,5):
        A.digitalWrite(red, A.HIGH)
        A.delay(1000)
        A.digitalWrite(red, A.LOW)
        A.delay(1000)
    return ('',200)

@app.route("/green")
def blinkGreen():
    for ii in range(0,5):
        A.digitalWrite(green, A.HIGH)
        A.delay(1000)
        A.digitalWrite(green, A.LOW)
        A.delay(1000)
    return ('',200)

if __name__ == "__main__":
    app.run(host="18.111.29.224", port=12345, debug=True)

