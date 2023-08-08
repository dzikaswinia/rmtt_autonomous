import robomaster
from robomaster import robot
import time

robomaster.config.LOCAL_IP_STR = "0.0.0.0"
drone = robot.Drone()
drone.initialize()
print('Drone initialized')

flight = drone.flight
flight.takeoff().wait_for_completed()
time.sleep(10)
flight.land().wait_for_completed()

print('Flight ended')
drone.close()