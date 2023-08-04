import time
import robomaster
from robomaster import robot

robomaster.config.LOCAL_IP_STR = "0.0.0.0"
drone = robot.Drone()
drone.initialize()
print('Drone initialized')

for i in range(0, 10):
    tof_info = drone.sensor.get_ext_tof()
    print(f'ext tof: {tof_info}') # getting None
    time.sleep(0.5)

drone.close()