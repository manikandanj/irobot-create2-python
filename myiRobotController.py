## References
 # https://petrimaki.com/2013/04/28/reading-arduino-serial-ports-in-windows-7/

import serial
import time
ser = serial.Serial('COM4', baudrate=115200, timeout=1)

while 1:
    command = raw_input("Enter a command: ")
    if(command == 'exit'):
        sys.exit('goodbye!')
    cmd = ""
    for v in command.split():
        cmd += chr(int(v))
    ser.write(cmd)
    #print ser.readline()
    time.sleep(1)