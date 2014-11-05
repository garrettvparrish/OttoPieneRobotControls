from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
import math, os, time, serial, time
import RPi.GPIO as GPIO

# initialize serial port
port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)

# wait 2 seconds
time.sleep(2)

### FLASK CONFIGURATION ###
tmpl_dir = '/home/pi/Desktop/OttoPieneRobotControls/'
app = Flask(__name__, template_folder=tmpl_dir, static_url_path='')
app.config['SECRET_KEY'] = 'lightballet'

### SOCKET CONFIRGURATION ###
socketio = SocketIO(app)

## SERIAL CONFIGURATION ### 
port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)

print "Serial connection initialized."

### GLOBAL VARIABLES ###

x = ''
y = ''
r = ''
lastAngle = 0
lastMotors = [1500,1500,1500]
defaultMotors = [1500,1500,1500]

### MOTOR CONTROL ###

# serial port helper function
def write(val):
    port.write(chr(val & 0xff))

# dir : 0 = forward, 1 = backwards
# id : motor number (128, 129, 130)
# val : 0 - 127
def motorCommand(id, dir, val):
    write(id)
    write(dir)
    write(val)
    write((id + dir + val) & 0b01111111)
    time.sleep(.1)

# mapping function to control the motors
def writeToMotors(x, y ,r):
    _r = int(float(r) * 127)
    motorCommand(128, 1, _r)
    motorCommand(129, 1, _r)
    motorCommand(130, 1, _r)

### FLASK SERVER ###

@app.route('/')
def index():
    return render_template('main.html')

### SOCKETS ###

@socketio.on('control')
def updateValues(message):
    global x,y,r
    message = message['data']
    x,y,r = message.split(',')
    print x + y  + r
    writeToMotors(x, y, r)
#    emit('motor1', r)
#    emit('motor2', x)
#    emit('motor3', y)

@socketio.on('connect')
def connect(message):
    print message['data']

@socketio.on('disconnect')
def disconnect():
    print 'Client disconnected'

if __name__ == '__main__':
    socketio.run(app, host = '0.0.0.0')

