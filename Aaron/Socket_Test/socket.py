from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
import math, os, time, logging
logging.basicConfig()

tmpl_dir = '/home/pi/Desktop/OttoPieneRobotControls/Aaron/Socket_Test' #os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
app = Flask(__name__, template_folder=tmpl_dir, static_url_path='')
app.config['SECRET_KEY'] = 'lightballet'
socketio = SocketIO(app)

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

@app.route('/')
def index():
    return render_template('main.html')

@socketio.on('control')
def updateValues(message):
    global x,y,r
    message = message['data']
    x,y,r = message.split(',')
    # deal with velocities and write to motors

    # DO IT HERE
    
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

#############################################
    
#DEVICE = '/dev/ttyACM0'
#BAUD = 9600
#ser = serial.Serial(DEVICE, BAUD)

#def takeGyroReading():
#    gyroAngle =  ser.read()
#    
#    return int(gyroAngle)

def translation(x,y):
    motors = [1500,1500,1500]
    
    x = ((x + 1)*1000) / 2 + 1000 # map x between 1000 and 2000
    y = ((y + 1)*1000) / 2 + 1000 # map y between 1000 and 2000

    xMove = translateX(x)
    yMove = translateY(y)
    
    for ii in range(3):
        motors[ii] = (xMove[ii] + yMove[ii])/2
    
    return motors

def translateX(x):
    return [3000-x,3000-x,x]
    
def translateY(y):
    return [y,y,1500] # 1 and 2 go full speed ahead and 3 does nothing

def rotation(r):
    #currentAngle = takeGyroReading()

    
    
    r = ((r + 1)*1000) / 2 + 1000 # map r between 1000 and 2000
    return [r, r, r]

def smoothMotors(currentMotors):
    global lastMotors

    for ii in range(3):
        if currentMotors[ii] < lastMotors[ii]:
            currentMotors[ii] -= 1
        elif currentMotors[ii] > lastMotors[ii]:
            currentMotors[ii] += 1

    lastMotors = currentMotors
    return currentMotors



