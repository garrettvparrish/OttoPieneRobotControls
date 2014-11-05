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

rVal,rDir = 0,0
xVal,xDir = 0,0
yVal,yDir = 0,0
@app.route('/motors')
def motors():
    # DIR: 0 FWD, 1 REV
    global rVal,rDir,xVal,xDir,yVal,yDir
    m1,m2,m3 = False,False,False
    if request.args.get('rVal') is not None:
        rVal = int(float(request.args.get('rVal')))
        m1 = True
    if request.args.get('rDir') is not None:
        rDir = int(float(request.args.get('rDir')))
        m1 = True
    if request.args.get('xVal') is not None:
        xVal = int(float(request.args.get('xVal')))
        m2 = True
    if request.args.get('xDir') is not None:
        xDir = int(float(request.args.get('xDir')))
        m2 = True
    if request.args.get('yVal') is not None:
        yVal = int(float(request.args.get('yVal')))
        m3 = True
    if request.args.get('yDir') is not None:
        yDir = int(float(request.args.get('yDir')))
        m3 = True

    if m1 is True:
        motorCommand(128, rDir, rVal)
    if m2 is True:
        motorCommand(129, xDir, xVal)
    if m3 is True:
        motorCommand(130, yDir, yVal)

    return('M1 %d %d, M2 %d %d, M3 %d %d' % (rVal,rDir,xVal,xDir,yVal,yDir))

@app.route('/motorstop')
def motorstop():
    global rVal,rDir,xVal,xDir,yVal,yDir
    rVal,rDir,xVal,xDir,yVal,yDir = 0,0,0,0,0,0
    motorCommand(128, 0, 0)
    motorCommand(129, 0, 0)
    motorCommand(130, 0, 0)
    return('ok')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

