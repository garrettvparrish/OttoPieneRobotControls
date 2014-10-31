import math
import serial

#DEVICE = '/dev/ttyACM0'
#BAUD = 9600
#ser = serial.Serial(DEVICE, BAUD)

lastAngle = 0
lastMotors = [1500,1500,1500]
defaultMotors = [1500,1500,1500]

def controlMotors(x,y,r):
    x = float(x)
    y = float(y)
    r = float(r)
    
    motors = [1500,1500,1500]
    trans = translation(x,y)
    rot = rotation(r)
    
    for ii in range(3):
        motors[ii] = int((trans[ii] + rot[ii])/2)
        
    motors = smoothMotors(motors)
    #print motors
    #motorString = motors[0] .",".motors[1].",".motors[2]
    #ser.write(motorString)
    return motors

#def takeGyroReading():
#    gyroAngle =  ser.read()
#    
#    return int(gyroAngle)

def translation(x,y):
    motors = [1500,1500,1500]
    
    x = ((x + 1)*1000) / 2 + 1000 # map x between 1000 and 2000
    y = ((y + 1)*1000) / 2 + 1000 # map y between 1000 and 2000

    xMove = translateX(x)
    yMove = translateY(y)
    
    for ii in range(3):
        motors[ii] = (xMove[ii] + yMove[ii])/2
    
    return motors

def translateX(x):
    return [3000-x,3000-x,x]
    
def translateY(y):
    return [y,y,1500] # 1 and 2 go full speed ahead and 3 does nothing

def rotation(r):
    #currentAngle = takeGyroReading()

    
    
    r = ((r + 1)*1000) / 2 + 1000 # map r between 1000 and 2000
    return [r, r, r]

def smoothMotors(currentMotors):
    global lastMotors

    for ii in range(3):
        if currentMotors[ii] < lastMotors[ii]:
            currentMotors[ii] -= 1
        elif currentMotors[ii] > lastMotors[ii]:
            currentMotors[ii] += 1

    lastMotors = currentMotors
    return currentMotors
