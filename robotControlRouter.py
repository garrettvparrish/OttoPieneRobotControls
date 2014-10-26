from flask import Flask, render_template, request
from nanpy import Arduino as A
import os
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')

app = Flask(__name__, template_folder=tmpl_dir, static_url_path='')
import datetime

red = 8
green = 11
A.pinMode(red, A.OUTPUT)
A.pinMode(green, A.OUTPUT)

@app.route("/", methods=['GET'])
def index():
    x = request.args.get('x')
	y = request.args.get('y')
    r = request.args.get('r')
    print str(x) + " " + str(y) + " " + str(r)
    return render_template('main.html', **templateData)

@app.route("/red")
def blinkRed():
    for ii in range(0,5):
        A.digitalWrite(red, A.HIGH)
        A.delay(1000)
        A.digitalWrite(red, A.LOW)
        A.delay(1000)
    return ('',200)

@app.route("/green")
def blinkGreen():
    for ii in range(0,5):
        A.digitalWrite(green, A.HIGH)
        A.delay(1000)
        A.digitalWrite(green, A.LOW)
        A.delay(1000)
    return ('',200)

if __name__ == "__main__":
    app.run(host="18.111.29.224", port=12345, debug=True)


# #include <SPI.h>
# #include <Wire.h>
# #include <L3G.h>
# #ifndef __arm__
# #include <avr/pgmspace.h>
# #else
# #define PROGMEM const
# #define F(x) x
# #endif
# #include <Servo.h>

# L3G gyro;

# int gyroSum = 0;
# float gyroOffset = 0;
# int Xval = 0;

# //gyro calibration variables
# int gyromin = -25000;
# int gyromax = 25000;

# //gyroscope smoothing variables
# int i = 0;
# float gyroaverage  = 0.;
# int numReadings = 5;
# long Xval_total = 0;
# int noisefloor = 100;
# int spinError = 0;

# //robot control variables

# Servo servo1; //front motor
# Servo servo2; //back right motor
# Servo servo3; //back left motor

# unsigned const int LEDf1 = 13;
# unsigned const int LEDb1 = 12;
# unsigned const int LEDf2 = 11;
# unsigned const int LEDb2 = 10;
# unsigned const int LEDf3 = 9;
# unsigned const int LEDb3 = 8;

# const int timeout = 10; //if no signal from controller, wait for 10 loops before stopping.
# int timecount = 0;
# int lasttimecount = 0;

# #define sqrt3_2  0.866
# #define pi  3.141
# const float  PI_2 =  6.283;

# float m1scale = 1.0;
# float m2scale = 1.0;
# float m3scale = 1.0;

# const int m1max = 2000;
# const int m1min = 1000;
# const int m2max = 2000;
# const int m2min = 1000;
# const int m3max = 2000;
# const int m3min = 1000;




# //const int m1max = 1875;
# //const int m1min = 1075;
# //const int m2max = 1980;
# //const int m2min = 1000;
# //const int m3max = 1950;
# //const int m3min = 1050;

# float thetaScale = 0.;
# float thetaCommand = 0.;
# float theta = 0.;
# const int motor1 = 9; //front motor
# const int motor2 = 6; //back right motor
# const int motor3 = 5; //back left motor
# const int pwmthresh = 10;
# float lasttheta = 0.;
# float RCommand = 0.;
# float R = 0.;
# float lastR = 0.;

# int lastpwm1a = 0;
# int lastpwm2a = 0;
# int lastpwm3a = 0;



# const int operationRange = 200;

# const int neutral1 = 1500;
# const int neutral2 = 1500;
# const int neutral3 = 1500;

# //const int neutral1 = 1480;
# //const int neutral2 = 1480;
# //const int neutral3 = 1450;

# int pwm1 = 1500;
# int pwm2 = 1500;
# int pwm3 = 1500;
# int spinCommand = 0;
# int spin = 0;
# int lastSpin = 0;

# int SPint = 0;
# int lastSPint = 0;
# int UDint = 0;
# int lastUDint = 0;
# int LRint = 0;
# int lastLRint = 0;

# //const int sensorPin = A0; //inputsensor
# const int analogLed = 3;
# const int threshold = 10;

# //char datapacket[3] = {' ', ' ', ' '};
# int dataSet = 0;
# int lastdataSet = 0;
# int lastSensorReading = 0;
# int nextpoint = 0;
# String inputString = "";
# String lastinputString = "";
# String datapacket = "";

# String UDstring = "";
# String lastUDstring = "";
# String LRstring = "";
# String lastLRstring = "";
# String SPstring = "";
# String lastSPstring = "";


# int updownval;
# int lastupdownval;
# int leftrightval;
# int lastleftrightval;
# int spinval;
# int lastspinval;



# void setup() {

#   Serial.begin(9600);

#   // robot setup
#   pinMode(LEDf1, OUTPUT);
#   pinMode(LEDb1, OUTPUT);
#   pinMode(LEDf2, OUTPUT);
#   pinMode(LEDb2, OUTPUT);
#   pinMode(LEDf3, OUTPUT);
#   pinMode(LEDb3, OUTPUT);

#   servo1.attach(motor1);
#   servo2.attach(motor2);
#   servo3.attach(motor3);

#   digitalWrite(LEDf1, HIGH);

#   servo1.writeMicroseconds(neutral1);
#   servo2.writeMicroseconds(neutral2);
#   servo3.writeMicroseconds(neutral3);

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

#     servo1.writeMicroseconds(neutral1);
#     servo2.writeMicroseconds(neutral2);
#     servo3.writeMicroseconds(neutral3);

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

#   servo1.writeMicroseconds(pwm1);
#   //analogWrite(13, map(constrain(pwm1, neutral1, 1950), neutral1, 1950, 0, 255));
#   //analogWrite(12,255- map(pwm1, neutral1, 1050, 255, 0));
#   servo2.writeMicroseconds(pwm2);
#   //analogWrite(11, map(constrain(pwm2, neutral2, 1950), neutral2, 1950, 0, 255));
#   //analogWrite(10,255- map(pwm2, neutral2, 1050, 255, 0));
#   servo3.writeMicroseconds(pwm3);
#   //analogWrite(9, map(constrain(pwm3, neutral3, 1950), neutral3, 1950, 0, 255));
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

#   servo1.writeMicroseconds(pwm1);
#   servo2.writeMicroseconds(pwm2);
#   servo3.writeMicroseconds(pwm3);

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



