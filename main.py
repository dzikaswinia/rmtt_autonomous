#import tello_sdk
import robomaster
from robomaster import robot
from robomaster import version

#ver = version.__version__
print('Trying to get SDK version')
#print(f'SDK version: {ver}')

robomaster.config.LOCAL_IP_STR = "0.0.0.0"

drone = robot.Drone()
drone.initialize()

ver = drone.get_sdk_version()
print(f'SDK version: {ver}')
drone.close()
