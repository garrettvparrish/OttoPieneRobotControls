from flask import Flask, render_template, request
from nanpy import Arduino as A
from nanpy import (SPI, Wire, L3G, Servo)
import os
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')

app = Flask(__name__, template_folder=tmpl_dir, static_url_path='')
import datetime

red = 8
green = 11
A.pinMode(red, A.OUTPUT)
A.pinMode(green, A.OUTPUT)

#####################
####### Gyro ########
#####################

L3G gyro
gyroSum = 0
gyroOffset = 0.0
Xval = 0

# gyro calibration variables
gyromin = -25000
gyromax = 25000

# gyro smoothing variables
i = 0
gyroaverage  = 0.
numReadings = 5
Xval_total = 0
noisefloor = 100
spinError = 0

#####################
###### MOTORS #######
#####################

# Motors 
Servo motor1 # front
Servo motor2 # back right
Servo motor3 # back left

# Motor Pins
motor1 = 9 # front motor
motor2 = 6 # back right motor
motor3 = 5 # back left motor

# Minimum and maximum motor values
m1max = 2000
m1min = 1000
m2max = 2000
m2min = 1000
m3max = 2000
m3min = 1000

# Scales
m1scale = 1.0
m2scale = 1.0
m3scale = 1.0

#####################
##### Control #######
#####################

lastpwm1a = 0
lastpwm2a = 0
lastpwm3a = 0

neutral1 = 1500
neutral2 = 1500
neutral3 = 1500

pwm1 = 1500
pwm2 = 1500
pwm3 = 1500
spinCommand = 0
spin = 0
lastSpin = 0

UDstring = ""
lastUDstring = ""
LRstring = ""
lastLRstring = ""
SPstring = ""
lastSPstring = ""

updownval
lastupdownval
leftrightval
lastleftrightval
spinval
lastspinval

SPint = 0
lastSPint = 0
UDint = 0
lastUDint = 0
LRint = 0
lastLRint = 0

analogLed = 3
threshold = 10

thetaScale = 0.
thetaCommand = 0.
theta = 0.
pwmthresh = 10
lasttheta = 0.
RCommand = 0.
R = 0.
lastR = 0.
operationRange = 200

dataSet = 0
lastdataSet = 0
lastSensorReading = 0
nextpoint = 0
inputString = ""
lastinputString = ""
datapacket = ""

# LEDs
LEDf1 = 13;
LEDb1 = 12;
LEDf2 = 11;
LEDb2 = 10;
LEDf3 = 9;
LEDb3 = 8;

# Timeouts
timeout = 10; # if no signal from controller, wait for 10 loops before stopping.
timecount = 0;
lasttimecount = 0;

# Constants
sqrt3_2 = 0.866
pi = 3.141
PI_2 = 6.283;

@app.route("/", methods=['GET'])
def index():
    	x = request.args.get('x')
	y = request.args.get('y')
    	r = request.args.get('r')
        templateData = {}
    	print str(x) + " " + str(y) + " " + str(r)
    	return render_template('main.html', **templateData)

@app.route("/update/<float:x>")
def updateX():
        print x
        return (x, 200)

@app.route("/update/<float:y>")
def updateY():
        print x
        return (x, 200)

@app.route("/update/<float:r>")
def updateR():
        print x
        return (x, 200)


if __name__ == "__main__":
    app.run(host="18.111.29.224", port=12345, debug=True)

# void setup() {

#   Serial.begin(9600);

#   motor# attach);
#   motor2.# attach(motor2;
#   motor3. # back left

#   digitalWrite(LEDf1, HIGH);

# # motor1(neutral1);
# #   motor2(neutral2);
#   motor3. # back left

#   delay(5000);

#   digitalWrite(LEDf1, LOW);

#   //gyro initialization

#   Wire.begin();

#   if (!gyro.init()) {
#     //    Serial.println("Failed to autodetect gyro type!");
#     //    while (1);
#   }

#   //  gyro.writeReg(L3G_CTRL_REG4, 0x02); // 2000 dps full scale
#   //  gyro.writeReg(L3G_CTRL_REG1, 0x0F); // normal power mode, all axes enabled, 100 Hz

#   gyro.enableDefault();
#   delay(100);

#   for (int i = 0; i < 50; i++) {
#     calibrateGyro();
#   }

#   gyroOffset = gyroSum / 50;
#   Serial.print("gyroOffset = ");
#   Serial.println(gyroOffset);
#   delay(100);

#   //setDestination();
#   delay(10000);
# }






# void loop() {


#     if (Serial.available() > 0) {
#       handleSerial();
#       delay(1);
#       correctRotaion();
#       timecount = 0;
#     }

# if (Serial.available() <= 0){
  
#     if (Serial.available() <= 0 && abs(timecount) <= timeout) {
#       correctRotaion();
#       timecount += 1;
#     }
  

#   else {

#   # motor1(neutral1);
# #     motor2(neutral2);
#     motor3. # back left

#     pwm1 = neutral1;
#     pwm2 = neutral2;
#     pwm3 = neutral3;

#     analogWrite(13, 0);
#     analogWrite(12, 0);
#     analogWrite(11, 0);
#     analogWrite(10, 0);
#     analogWrite(9, 0);
#     analogWrite(8, 0);

#     timecount += 1;
#   }
# }
# }










# void calibrateGyro() {
#   gyro.read();

#   gyroSum += (int)gyro.g.x;
#   Serial.print("gyroSum = ");
#   Serial.println(gyroSum, DEC);
#   delay(10);
# }

# void setDestination() {
#   Serial.print("+++");
#   char thisByte = 0;

#   while (thisByte != '\r') {
#     if (Serial.available() > 0) {
#       thisByte = Serial.read();
#     }
#   }
#   Serial.print("ATDH0, DL9666\r");
#   Serial.print("ATMY2654\r");
#   Serial.print("ATID8733\r");
#   Serial.println("ATCN\r");
#   delay(10);
#   lasttimecount = millis();
# }






# void calculateSpeed() {

#   //  speed control and damping
#   float UDinta = float((UDint) + 2 * lastUDint) / 3;
#   float LRinta = float((LRint) + 2 * lastLRint) / 3;

#   R = constrain(sqrt(pow(LRinta, 2) + pow(UDinta, 2)) / 512., 0, 1);

#   //  spin control and damping
#   spinCommand = map(SPint, -512, 512, -300, 300);

#   if (spinCommand - lastSpin > 100) {
#     spin = lastSpin + 100;
#   }

#   if (spinCommand - lastSpin < -100) {
#     spin = lastSpin - 100;
#   }

#   if (spinCommand - lastSpin >= -100 && spinCommand - lastSpin <= 100) {
#     spin = spinCommand;
#   }

#   // rotation feedback
#   takeGyroreading();
#   int rotation = map(gyroaverage, gyromin, gyromax, -180, 180);
#   spinError =  rotation - lastSpin;

#   //  angle definitions

#   // quadrant one (forward left)
#   if (LRinta >= 0 && UDinta >= 0) {
#     theta = abs(atan(UDinta / LRinta));
#   }

#   // quadrant two (back left)
#   if (LRinta < 0 && UDinta >= 0)  {
#     theta = pi - abs(atan(UDinta / LRinta));
#   }

#   // quadrarnt three (back right)
#   if (LRinta < 0 && UDinta < 0) {
#     theta = pi + abs(atan(UDinta / LRinta));
#   }

#   // quadrant four (forward right)
#   if (LRinta >= 0 && UDinta < 0) {
#     theta = 2 * pi - abs(atan(UDinta / LRinta));
#   }

#   // motor speed computations
#   int pwm1a = int(cos(theta) * R * 2000);
#   int pwm2a = int((-.5 * cos(theta) + sqrt3_2 * sin(theta)) * R * 2000);
#   int pwm3a = int((-.5 * cos(theta) - sqrt3_2 * sin(theta)) * R * 2000);

#   //  motor speed mapping
#   pwm1 = map(pwm1a, -2000, 2000, m1min, m1max) + (neutral1 - 1500) + spinError;
#   pwm2 = map(pwm2a, -2000, 2000, m2min, m2max) + (neutral2 - 1500) + spinError;
#   pwm3 = map(pwm3a, -2000, 2000, m3min, m3max) + (neutral3 - 1500) + spinError;

#   //  pwm1 = constrain(map(pwm1a, -1000, 1000, m1min, m1max) + (neutral1-1500) + spin, 1000, 2000);
#   //  pwm2 = constrain(map(pwm2a, -1000, 1000, m2min, m2max) + (neutral2-1500) + spin, 1000, 2000);
#   //  pwm3 = constrain(map(pwm3a, -1000, 1000, m3min, m3max) + (neutral3-1500) + spin, 1000, 2000);

#   motor1.writeMicroseconds(pwm1);
#   //analogWrite(13, map(constrain(pwm1, neutral1, 1950), neutral1, 1950, 0, 255));
#   //analogWrite(12,255- map(pwm1, neutral1, 1050, 255, 0));
#   motor# writeMicroseconds);
#   //analogWrite(11, map(constrain(pwm2, # neutral2,), neutral2, 1950, 0, 255));#   //analog
Write(10,255- map(pwm2, neutral2, 1050, 255, 0)); # back left
#   motor3.ogWrite(9, map(constrain(pwm3, neutral3, 1950), neutral3, 1950, 0, 255));
#   //analogWrite(8,255- map(pwm3, neutral3, 1050, 255, 0));

#   //  values stored for next loop of program

#   lasttheta = theta;
#   lastR = R;
#   lastSpin = spin;

#   lastpwm1a = pwm1a;
#   lastpwm2a = pwm2a;
#   lastpwm3a = pwm3a;

#   //Serial.print(gyroaverage);
#   //Serial.print("     ");
#   //Serial.print(pwm1);
#   //Serial.print("     ");
#   //Serial.print(pwm2);
#   //Serial.print("     ");
#   //Serial.print(pwm3);
# }




# void correctRotaion()
# {
#   takeGyroreading();
#   int rotation = map(gyroaverage, gyromin, gyromax, -180, 180);
#   spinError =  rotation - lastSpin;

#   pwm1 = map(lastpwm1a, -2000, 2000, m1min, m1max) + (neutral1 - 1500) + spinError;
#   pwm2 = map(lastpwm2a, -2000, 2000, m2min, m2max) + (neutral2 - 1500) + spinError;
#   pwm3 = map(lastpwm3a, -2000, 2000, m3min, m3max) + (neutral3 - 1500) + spinError;

# # motor1(pwm1);
# #   motor2(pwm2);
#   motor3. # back left

# }


# void handleSerial() {

#   char inByte = Serial.read();

#   //////// MOTOR 1
#   if (inByte == '@') {
#     dataSet = 2;
#     if (UDstring.toInt() > 0 && UDstring.toInt() <= 1024) {
#       UDint = map(UDstring.toInt(), 0, 1024, -512, 512);
#       //if (abs(UDint-lastUDint) < pwmthresh){
#       //      pwm1 = map(UDstring.toInt(), 1, 1024, 1000, 2000);
#       //      if (abs(pwm1-1500) <= pwmthresh){
#       //        pwm1 = 1500;
#       //      }
#       //  Serial.print(" pwm1: ");
#       //    Serial.print(pwm1);
#       // }

#     }
#     UDstring = "";
#   }

#   //////// MOTOR 2

#   if (inByte == '#') {
#     dataSet = 3;
#     if (LRstring.toInt() > 0 && LRstring.toInt() <= 1024) {
#       LRint = map(LRstring.toInt(), 0, 1024, 512, -512);
#       // if (abs(LRint-lastLRint) < pwmthresh){
#       //      pwm2 = map(LRstring.toInt(), 1, 1024, 1000, 2000);
#       //      if (abs(pwm2-1500) <= pwmthresh){
#       //        pwm2 = 1500;
#       //      }
#       //   Serial.print(" pwm2: ");
#       //    Serial.println(pwm2);
#       // }
#     }
#     LRstring = "";
#   }

#   //////// MOTOR 3

#   if (inByte == '!') {
#     dataSet = 1;
#     if (SPstring.toInt() > 0 && SPstring.toInt() <= 1024) {
#       SPint = map(SPstring.toInt(), 0, 1024, -512, 512);
#       //if (abs(SPint-lastSPint) < pwmthresh){
#       // pwm3 = map(SPstring.toInt(), 1, 1024, 1000, 2000);
#       //      if (abs(pwm3-1500) <= pwmthresh){
#       //        pwm3 = 1500;
#       //      }
#       //Serial.print(" pwm3: ");
#       //    Serial.print(pwm3);
#       // }
#     }
#     SPstring = "";
#   }

#   if (isDigit(inByte) > 0 && dataSet == lastdataSet) {
#     if (dataSet == 2) {
#       UDstring = lastUDstring + inByte;
#     } else if (dataSet == 1) {
#       LRstring = lastLRstring + inByte;
#     } else if (dataSet == 3) {
#       SPstring = lastSPstring + inByte;
#     }
#   }

#   if (LRint != lastLRint || UDint != lastUDint || SPint != lastSPint) {
#     calculateSpeed();
#   }

#   lastUDint = UDint;
#   lastLRint = LRint;
#   lastSPint = SPint;


#   lastUDstring = UDstring;
#   lastLRstring = LRstring;
#   lastSPstring = SPstring;

#   lastdataSet = dataSet;
# }




# void takeGyroreading() {
#   for (int i = 0; i < numReadings; i++) {
#     gyro.read();
#     Xval_total += (gyro.g.x - gyroOffset);
#   }

#   Xval = Xval_total / numReadings;

#   if (abs(Xval) >= noisefloor) {
#     gyroaverage = Xval;
#   }

#   else {
#     gyroaverage = 0;
#   }
# }



