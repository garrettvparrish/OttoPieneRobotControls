#include <SoftwareSerial.h>

#define DIGITAL_TRIGGER 9
#define INDICATOR_LED 13

SoftwareSerial initializationSerial(2,3); // Rx, Tx

void setup() {
  pinMode(DIGITAL_TRIGGER, INPUT);
  pinMode(INDICATOR_LED, OUTPUT);
  initializationSerial.begin(19200);
}

boolean triggered = false;

void loop() {
  
  if (digitalRead(DIGITAL_TRIGGER) == LOW) {
    delay(500);
    initializationSerial.write(170); // sets baud rate on controllers
    delay(500);
    triggered = !triggered;
    digitalWrite(INDICATOR_LED, HIGH);  
  } else {
    digitalWrite(INDICATOR_LED, LOW);
  }
}
