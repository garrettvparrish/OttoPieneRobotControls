from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

#from nanpy import Arduino as A
#from nanpy import (SPI, Wire, L3G, Servo)
import os
#tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')

app = Flask(__name__)#, template_folder=tmpl_dir, static_url_path='')
#app.config['SECRET_KEY'] = 'lightballet'
socketio = SocketIO(app)
import datetime

@app.route("/", methods=['GET'])
def index():
    	templateData = {}
	return render_template('main.html', **templateData)

# converts a string to an int. If that is not possible, it returns 0
def stringToInt(value):
    try:
        return int(float(value))
    except ValueError:
        return 0

@app.route("/")
def index():
    templateData = {}
    return render_template('main.html', **templateData)

@socketio.on('x', namespace = '/')
def getX(message):
    global x
    x = stringToInt(message)

@socketio.on('y', namespace = '/')
def getX(message):
    global y
    y = stringToInt(message)

@socketio.on('r', namespace = '/')
def getX(message):
    global r
    r = stringToInt(message)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0')

#takes an array of the current motor values and sends it over the socket
def updateController(motors):
    socketio.emit('motor1',{'data':motors[0]})
    socketio.emit('motor2',{'data':motors[1]})
    socketio.emit('motor3',{'data':motors[2]})

def updateMotors(x, y ,r):
    # where computation is done to actually turn the motors on
    _m1 = x
    _m2 = y
    _m2 = r
    # write values to motors
    # motor1.writeMicroseconds(_m1 * 1000 + 1000)
    # motor2.writeMicroseconds(_m2 * 1000 + 1000)
    # motor3.writeMicroseconds(_m3 * 1000 + 1000)

