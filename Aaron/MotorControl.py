import math
import serial

DEVICE = '/dev/ttyACM0'
BAUD = 9600
ser = serial.Serial(DEVICE, BAUD)

def ControlMotors(x,y,r):
    motors = [1500,1500,1500]
    trans = Translation(x,y)
    rot = Rotation(r)

    for ii in range(3):
        motors[ii] = (trans[ii] + rot[ii])/2

    motorString = motors[0] .",".motors[1].",".motors[2]
    ser.write(motorString)
    return

def TakeGyroReading():


def Translation(x,y):
    motors = [1500,1500,1500]
    
    x = ((x + 1)*1000) / 2 + 1000 # map x between 1000 and 2000
    y = ((y + 1)*1000) / 2 + 1000 # map y between 1000 and 2000

    xMove = TranslateX(x)
    yMove = TranslateY(y)
    
    for ii in range(3):
        motors[ii] = (xMove[ii] + yMove[ii])/2
    
    return motors

def TranslateX(x):
    return [-1*x,-1*x,x]
    
def TranslateY(y):
    return [y,y,1500] # 1 and 2 go full speed ahead and 3 does nothing

def Rotation(r):
    r = ((r + 1)*1000) / 2 + 1000 # map r between 1000 and 2000

    return [r, r, r]
