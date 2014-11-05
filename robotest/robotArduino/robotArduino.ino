#include <SoftwareSerial.h>

#define DIGITAL_TRIGGER 9
#define INDICATOR_LED 13

#define MOTOR1 (byte)128
#define MOTOR2 (byte)129
#define MOTOR3 (byte)130

#define FWD 0
#define REV 1

SoftwareSerial motorserial(2,3); // Rx, Tx

void setup() {
  pinMode(DIGITAL_TRIGGER, INPUT);
  pinMode(INDICATOR_LED, OUTPUT);
  motorserial.begin(19200);
}

boolean triggered = false;

void loop() { 
    if (!triggered) {
      delay(2500);
      motorserial.write(170); // sets baud rate on controllers
      delay(500);
      digitalWrite(INDICATOR_LED, HIGH);  
  
      delay(500);
      triggered = true;
    }
}

void motorcommand(byte id, byte dir, byte val) {
  motorserial.write(id); // address
  motorserial.write(dir); // direction
  motorserial.write(val); // speed 0-127

  motorserial.write((id + dir + val) & 0b01111111); // checksum
  delay(100);
}
