from flask import Flask, render_template, request
import math, os, time, serial, time
import RPi.GPIO as GPIO

# initialize serial port
port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)

# wait 2 seconds
#time.sleep(2)

### FLASK CONFIGURATION ###
tmpl_dir = '/home/pi/Desktop/OttoPieneRobotControls/'
app = Flask(__name__, template_folder=tmpl_dir, static_url_path='/static')
app.config['SECRET_KEY'] = 'lightballet'
app.config['DEBUG'] = True


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
    write(170)

    write(id)
    write(dir)
    write(val)
    write((id + dir + val) & 0b01111111)


# mapping function to control the motor
def writeToMotors(x, y ,r):
    _r = int(float(r) * 127)
    motorCommand(128, 1, _r)
    motorCommand(129, 1, _r)
    motorCommand(130, 1, _r)


### FLASK SERVER ###

@app.route('/')
def index():
    return app.send_static_file('foo.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    print request.args.get('foo')
    return('ok')

m1s,m1d = 0,0
m2s,m2d = 0,0
m3s,m3d = 0,0
@app.route('/motors')
def motors():
    global m1s,m1d,m2s,m2d,m3s,m3d
    m1,m2,m3 = False,False,False
    if request.args.get('m1s') is not None:
        m1s = int(float(request.args.get('m1s')))
        m1 = True
    if request.args.get('m1d') is not None:
        m1d = int(float(request.args.get('m1d')))
        m1 = True
    if request.args.get('m2s') is not None:
        m2s = int(float(request.args.get('m2s')))
        m2 = True
    if request.args.get('m2d') is not None:
        m2d = int(float(request.args.get('m2d')))
        m2 = True
    if request.args.get('m3s') is not None:
        m3s = int(float(request.args.get('m3s')))
        m3 = True
    if request.args.get('m3d') is not None:
        m3d = int(float(request.args.get('m3d')))
        m3 = True

    if m1 is True:
        motorCommand(128, m1d, m1s)
    if m2 is True:
        motorCommand(129, m2d, m2s)
    if m3 is True:
        motorCommand(130, m3d, m3s)

    return('M1 %d %d, M2 %d %d, M3 %d %d' % (m1s,m1d,m2s,m2d,m3s,m3d))

@app.route('/motorstop')
def motorstop():
    global m1s,m1d,m2s,m2d,m3s,m3d
    m1s,m1d,m2s,m2d,m3s,m3d = 0,0,0,0,0,0
    motorCommand(128, 0, 0)
    motorCommand(129, 0, 0)
    motorCommand(130, 0, 0)
    return('ok')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

