## Authors
 # Manikandan Jeyarajan

## References
 # Create2 Open Interface Spec - http://www.irobotweb.com/~/media/MainSite/PDFs/About/STEM/Create/iRobot_Roomba_600_Open_Interface_Spec.pdf?la=en
 # http://www.irobotweb.com/~/media/MainSite/PDFs/About/STEM/Create/Python_Tethered_Driving.pdf 
 # https://petrimaki.com/2013/04/28/reading-arduino-serial-ports-in-windows-7/

import serial
import time

# Add code to fetch COM port dynamically
COM_PORT = 'COM4'
DRIVE = '137'

def connectRobot():
	ser = serial.Serial(COM_PORT, baudrate=115200, timeout=1)

def __format_to_two_bytes(val):
	binformat = bin(val & 0b1111111111111111)
	hexformat = hex(int(binformat, 2))
	firstbyte, secondbyte = divmod(int(hexformat,16), 0x100)
	return str(firstbyte) + ' ' + str(secondbyte)

def __sendCommand(command):
	cmd = ""
    for v in command.split():
		cmd += chr(int(v))
    ser.write(cmd)
    time.sleep(1)
	
def driveRobot(velocity, radius):
	command = DRIVE + ' ' + __format_to_two_bytes(velocity) + ' ' + __format_to_two_bytes(radius)
	__sendCommand(command)

def driveForward(velocity):
	driveRobot(velocity, 32768)

def driveBackward():
	driveRobot(-1 * velocity, 32768)
	
def rotateClockwise(velocity):
	driveRobot(velocity, -1)

def rotateAntiClockwise(velocity):
	driveRobot(velocity, 1)
	
def parkRobot():
	driveRobot(0,0)

connectRobot()
while 1:
    command = raw_input("Enter a command: ")
    if(command == 'exit'):
        sys.exit('goodbye!')
	__sendCommand(command)