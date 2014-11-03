import serial
import time

time.sleep(2)

# initialize serial port
port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)

# wait 2 seconds
time.sleep(5)

# write to serial port
def write(val):
    port.write(chr(val & 0xff))

# configure motor controllers to determine baud rate
#write(0xaa)
##time.sleep(5)

# dir : 0 = forward, 1 = backwards
# id : motor number (128, 129, 130)
# val : 0 - 127
def motorCommand(id, dir, val):
    write(id)
    write(dir)
    write(val)
    write((id + dir + val) & 0b01111111)
    time.sleep(.1)
    print '%s %s %s' % (id, dir, val)

while True:
    motorCommand(128, 0, 50)
    time.sleep(2)
    motorCommand(128, 0, 0)

    motorCommand(129, 0, 50)
    time.sleep(2)
    motorCommand(129, 0, 0)

    motorCommand(130, 0, 50)
    time.sleep(2)
    motorCommand(130, 0, 0)

    motorCommand(128, 1, 50)
    time.sleep(2)
    motorCommand(128, 0, 0)

    motorCommand(129, 1, 50)
    time.sleep(2)
    motorCommand(129, 0, 0)

    motorCommand(130, 1, 50)
    time.sleep(2)
    motorCommand(130, 0, 0)

