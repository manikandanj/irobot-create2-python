## Simple program to demonstrate the usage of iRobotController
import iRobotController

iRobotController.getReady()
for i in range(1,5):
    iRobotController.driveForwardFor(3)
    iRobotController.turnRight()
iRobotController.finish()