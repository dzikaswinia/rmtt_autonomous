import time
import robomaster
from robomaster import robot

robomaster.config.LOCAL_IP_STR = "0.0.0.0"
drone = robot.Drone()
drone.initialize()
led = drone.led
led.set_led(r=0, g=0, b=0)
rgb_list = [(100,100,100), (255,255,255), (255,0,0), (0,255,0), (0,0,255)]
for rgb_info in rgb_list:
    led.set_led(r=rgb_info[0], g=rgb_info[1], b=rgb_info[2])
    time.sleep(0.5)

drone.close()
