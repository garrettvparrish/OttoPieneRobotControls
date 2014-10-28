from flask import Flask, render_template, request
from nanpy import Arduino as A
#from nanpy import (SPI, Wire, L3G, Servo)
import os
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')

app = Flask(__name__, template_folder=tmpl_dir, static_url_path='')
import datetime

red = 8
green = 11
A.pinMode(red, A.OUTPUT)
A.pinMode(green, A.OUTPUT)

# #####################
# ####### Gyro ########
# #####################

# L3G gyro
# gyroSum = 0
# gyroOffset = 0.0
# Xval = 0

# # gyro calibration variables
# gyromin = -25000
# gyromax = 25000

# #####################
# ###### MOTORS #######
# #####################

# # Motors 
# Servo motor1 # front
# Servo motor2 # back right
# Servo motor3 # back left

# # Motor Pins
# motor1 = 9 # front motor
# motor2 = 6 # back right motor
# motor3 = 5 # back left motor

# # Minimum and maximum motor values
# m1max = 2000
# m1min = 1000
# m2max = 2000
# m2min = 1000
# m3max = 2000
# m3min = 1000

# # Scales
# m1scale = 1.0
# m2scale = 1.0
# m3scale = 1.0

# #####################
# ##### Control #######
# #####################

# lastpwm1a = 0
# lastpwm2a = 0
# lastpwm3a = 0

# neutral1 = 1500
# neutral2 = 1500
# neutral3 = 1500

@app.route("/", methods=['GET'])
def index():
    	templateData = {}
	return render_template('main.html', **templateData)

# ?key=value
@app.route("/update", methods=['POST', 'GET'])
def update():
    x = request.args.get('x')
    y = request.args.get('y')
    r = request.args.get('r')

    # update motors
    updateMotors(x,y,r)

    print str(x) + " " + str(y) + " " + str(r)
    return (x, 200)

if __name__ == "__main__":
    app.run(host="18.111.29.224", port=12345, debug=True)


def updateMotors(x, y ,r):
    # where computation is done to actually turn the motors on
    _m1 = x
    _m2 = y
    _m2 = r
    # write values to motors
    # motor1.writeMicroseconds(_m1 * 1000 + 1000)
    # motor2.writeMicroseconds(_m2 * 1000 + 1000)
    # motor3.writeMicroseconds(_m3 * 1000 + 1000)

