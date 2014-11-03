#include <SoftwareSerial.h>

#define DIGITAL_TRIGGER 9

SoftwareSerial initializationSerial(2,3); // Rx, Tx

void setup() {
	pinMode(DIGITAL_TRIGGER, INPUT);

	initializationSerial.begin(19200);
}


boolean triggered = false;

void loop() {

	if (digitalRead(DIGITAL_TRIGGER) == HIGH && !triggered) {
		delay(500);
		initializationSerial.write(170); // sets baud rate on controllers
		delay(500);
		triggered = !triggered;
	} 
}
