#include <SoftwareSerial.h>

#define MOTOR1 (byte)128
#define MOTOR2 (byte)129
#define MOTOR3 (byte)130

#define FWD 0
#define REV 1

#define MAX_SPEED 127

SoftwareSerial motorserial(2,3); // Rx, Tx
void setup() {
  delay(5000); // MUST wait at least 2 seconds before sending the baud rate byte below
  
  motorserial.begin(19200); // 38400 was a little unreliable, this seems to work
  delay(500);
  
  motorserial.write(170); // sets baud rate on controllers
  delay(500);
}

void loop() {
  if (true) {
    motorcommand(MOTOR1, FWD, 50);
    motorcommand(MOTOR2, FWD, 50);
    motorcommand(MOTOR3, FWD, 50);
    delay(2000);
  
    motorcommand(MOTOR1, FWD, 0);
    motorcommand(MOTOR2, FWD, 0);
    motorcommand(MOTOR3, FWD, 0);
    delay(500);
    
    motorcommand(MOTOR1, REV, 50);
    motorcommand(MOTOR2, REV, 50);
    motorcommand(MOTOR3, REV, 50);
    
    delay(2000);
    
    motorcommand(MOTOR1, FWD, 0);
    motorcommand(MOTOR2, FWD, 0);
    motorcommand(MOTOR3, FWD, 0);
    delay(500);
  }
}

void motorcommand(byte id, byte dir, byte val) {
  motorserial.write(id); // address
  motorserial.write(dir); // direction
  motorserial.write(val); // speed 0-127

  motorserial.write((id + dir + val) & 0b01111111); // checksum
  delay(100);
}
