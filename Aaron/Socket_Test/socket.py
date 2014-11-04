from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
import math, os, time, logging, serial, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# initialize serial port
port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)

#### WRITE DIGITAL HIGH TO THE ARDUINO PAGE #### 
GPIO.setup(9, GPIO.OUT)
GPIO.output(9,1)
time.sleep(5)

# wait 2 seconds
time.sleep(2)

logging.basicConfig()

tmpl_dir = '/home/pi/Desktop/OttoPieneRobotControls/Aaron/Socket_Test' #os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
app = Flask(__name__, template_folder=tmpl_dir, static_url_path='')
app.config['SECRET_KEY'] = 'lightballet'
socketio = SocketIO(app)

## CONFIGURE SERIAL CONNECTION
port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)

print "Initialized..."
x = ''
y = ''
r = ''
lastAngle = 0
lastMotors = [1500,1500,1500]
defaultMotors = [1500,1500,1500]

# motor pins
m1 = 9
m2 = 10
m3 = 11

# write to serial port
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

@app.route('/')
def index():
    return render_template('main.html')

@socketio.on('control')
def updateValues(message):
    global x,y,r
    message = message['data']
    x,y,r = message.split(',')
    _r = int(float(r) * 127)

    # cap at zero
    
    # only send commands to the motors if they are ready to receive
    # (handshake from the arduino has been processed)

    # set motors to turn on (LEAAVE FOR NOW -- will just spin)
    motorCommand(128, 1, _r)
    motorCommand(129, 1, _r)
    motorCommand(130, 1, _r)
    
    emit('motor1', r)
    emit('motor2', x)
    emit('motor3', y)

@socketio.on('connect')
def connect(message):
    print message['data']

@socketio.on('disconnect')
def disconnect():
    print 'Client disconnected'

if __name__ == '__main__':
    socketio.run(app, host = '0.0.0.0')

