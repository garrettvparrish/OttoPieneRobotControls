import serial, time
#import RPi.GPIO as GPIO

ledPin = 16

#time.sleep(2)


print("Setting the GPIO pin modes and configuration. Sleeping for 5.")

# set the mode of the GPIO output pins
#GPIO.setmode(GPIO.BCM)

# configure LED pin
#GPIO.setup(ledPin, GPIO.OUT)

# setting it LOW will trigger the pin
#GPIO.output(ledPin, GPIO.LOW)

# configure motor controllers to determine baud rate
#time.sleep(1)

# set the pin to high again
#GPIO.output(ledPin, GPIO.HIGH)

#time.sleep(3)

print("Setting up the serial port. Sleeping for 2.")

# initialize serial port
port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)

# write to serial port
def write(val):
    port.write(chr(val & 0xff))

# wait 2 seconds
time.sleep(1)

# dir : 0 = forward, 1 = backwards
# id : motor number (128, 129, 130)
# val : 0 - 127
def motorCommand(id, dir, val):
    write(id)
    write(dir)
    write(val)
    write((id + dir + val) & 0b01111111)
    time.sleep(.1)

print("Sending motor commands")

while True:

    print("BCK")
    motorCommand(128, 1, 50)
    time.sleep(2)

    print("FWD")
    motorCommand(128, 0, 50)
    time.sleep(2)
