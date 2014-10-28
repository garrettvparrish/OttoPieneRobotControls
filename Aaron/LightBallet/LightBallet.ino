#include <SPI.h>
#include <Wire.h>
#include <L3G.h>
#include <Servo.h>

L3G gyro;

// Setup the gyro
int sampleNum = 1000;
int dc_offset = 0;
double noise = 0;
unsigned long time;
int sampleTime = 10;
int rate;
int prev_rate = 0;
double angle = 0;

// Setup the servos
Servo servo1;
Servo servo2;
Servo servo3;
int servo1_pin = 1;
int servo2_pin = 2;
int servo3_pin = 3;
int defaultMotorValues[3] = {1500, 1500, 1500};
int motorValues[3];
String serialString = "";
char character;

void setup() {
 
  // Attach the Servos
  servo1.attach(servo1_pin);
  servo2.attach(servo2_pin);
  servo3.attach(servo3_pin);
   
  Serial.begin(9600);
  Wire.begin();
  if(!gyro.init()){
    Serial.println("Failed to autodetect gyro type");
  }
  
  // Calibrate the gyro

  for(int n=0; n<sampleNum; n++){
    gyro.read();
    dc_offset += (int)gyro.g.x;
  }
  dc_offset = dc_offset/sampleNum;
  
  for(int n=0; n<sampleNum; n++){
    gyro.read();
    if((int)gyro.g.x-dc_offset>noise)
      noise=(int)gyro.g.x-dc_offset;
    else if((int)gyro.g.x-dc_offset<-noise)
    noise=-(int)gyro.g.x-dc_offset;
  }

  noise=noise/100; //gyro returns hundredths of degrees/sec
  //print dc offset and noise level

  Serial.println();
  Serial.print("DC Offset: ");
  Serial.print(dc_offset);
  Serial.print("\tNoise Level: ");
  Serial.print(noise);
  Serial.println();
}

void loop(){
  // Read motor values from the serial and send them to the motors
  if (Serial.available()){
    serialString = "";
    while(Serial.available()){
      character = Serial.read();
      serialString.concat(character);
    }
    for(int i = 0; i < 3; i++){
      int index = serialString.indexOf(","); //We find the next comma
      motorValues[i] = atol(serialString.substring(0,index).c_str()); //Extract the number
      serialString = serialString.substring(index+1); //Remove the number from the string
    }
  }
  else{
    motorValues[0] = defaultMotorValues[0];
    motorValues[1] = defaultMotorValues[1];
    motorValues[2] = defaultMotorValues[2];
  }
  
   servo1.write(motorValues[0]);
   servo2.write(motorValues[1]);
   servo3.write(motorValues[2]);
   
   // Send Gyro values to the pi for processing

  if(millis() - time > sampleTime){
    time = millis(); // update the time to get the next sample
    gyro.read();
    rate = ((int)gyro.g.x - dc_offset)/100;
    
    angle += (double)((prev_rate + rate) / 100));
    
    prev_rate = rate;
    
    if(angle < 180){
      angle += 360;
    }
    else if (angle >= 360){
      angle -= 360;
    }
    Serial.print("angle: ");
    Serial.println(angle);
  }
}
