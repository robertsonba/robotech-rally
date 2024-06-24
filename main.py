import machine
import PicoMotorDriver
import network
import socket
from time import sleep

board = PicoMotorDriver.KitronikPicoMotor()
# forward_bumper = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)

def forward():
    board.motorOn(1, "r", 75)
    board.motorOn(2, "r", 75)
    
def reverse():
    board.motorOn(1, "f", 75)
    board.motorOn(2, "f", 75)
    
def left():
    board.motorOn(1, "r", 75)
    board.motorOn(2, "f", 75)

def right():
    board.motorOn(1, "f", 75)
    board.motorOn(2, "r", 75)

def stop():
    board.motorOff(1)
    board.motorOff(2)
    
# Import the 
exec(open("RACE.py").read())

# connect the wifi
exec(open("connectWifi.py").read())

