from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
import MotorControl as control

import logging
logging.basicConfig()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lightballet'
socketio = SocketIO(app)

x = ''
y = ''
r = ''

@app.route('/')
def index():
    return render_template('main.html')

@socketio.on('control')
def updateValues(message):
    global x,y,r
    message = message['data']
    x,y,r = message.split(',')
        
    motors = control.controlMotors(x,y,r)
    emit('motor1',motors[0])
    emit('motor2',motors[1])
    emit('motor3',motors[2])

##@socketio.on('x')
##def updateX(message):
##    global x
##    x = message['data']
##    print x
##
##@socketio.on('y')
##def updateY(message):
##    global y
##    y = message['data']
##    print y
##
##@socketio.on('r')
##def updateR(message):
##    global r
##    r = message['data']
##    print r

@socketio.on('connect')
def connect(message):
    print message['data']

@socketio.on('disconnect')
def disconnect():
    print 'Client disconnected'

if __name__ == '__main__':
    socketio.run(app, host = '0.0.0.0')
