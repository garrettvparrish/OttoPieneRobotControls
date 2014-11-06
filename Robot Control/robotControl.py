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

FWD = 0
REV = 1
COS60 = .5
SIN30 = .5
COS30 = .866
SIN60 = .866

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
        rVal = float(request.args.get('rVal'))
    if request.args.get('rDir') is not None:
        rDir = int(float(request.args.get('rDir')))
    if request.args.get('xVal') is not None:
        xVal = int(float(request.args.get('xVal')))
    if request.args.get('xDir') is not None:
        xDir = int(float(request.args.get('xDir')))
    if request.args.get('yVal') is not None:
        yVal = int(float(request.args.get('yVal')))
    if request.args.get('yDir') is not None:
        yDir = int(float(request.args.get('yDir')))

    # strip out the inital velocities
    Vr = int(rVal * 127.0/3.0) # split equally between all three motors --> all same
    Vx = xVal if (xDir == FWD) else -1.0*xVal # horizontal velocity
    Vy = yVal if (yDir == FWD) else -1.0*yVal # vertical velocity

    # MOTOR 1
    m1Vx = Vx / 2.0 
    m1Vy = 0

    m1Val = Vr + m1Vx + m1Vy
    m1Dir = REV if (m1Val < 0) else FWD
    motorCommand(128, m1Dir, int(math.fabs(m1Val)))

    # MOTOR 2
    m2Vx = (-1.0 * COS60 * Vx / 2.0) / 2.0 * 127
    m2Vy = Vy / (COS30 * 2.0)

    m2Val = Vr + m2Vx + m2Vy
    m2Dir = REV if (m2Val < 0) else FWD
    motorCommand(129, m2Dir, int(math.fabs(m2Val)))

    # MOTOR 3
    m3Vx = (-1.0 * COS60 * Vx / 2.0) / 2.0 * 127
    m3Vy = -1.0 * Vy / (COS30 * 2.0)

    m3Val = Vr + m3Vx + m2Vy
    m3Dir = REV if (m3Val < 0) else FWD
    motorCommand(130, m3Dir, int(math.fabs(m3Val)))

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

