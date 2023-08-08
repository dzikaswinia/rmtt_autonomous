import robomaster
from robomaster import robot
import time

robomaster.config.LOCAL_IP_STR = "0.0.0.0"
drone = robot.Drone()
drone.initialize()
print('Drone initialized')

flight = drone.flight
flight.takeoff().wait_for_completed()
flight.up(distance=30).wait_for_completed()
flight.forward(distance=100).wait_for_completed()
flight.down(distance=30).wait_for_completed()
flight.forward(distance=60).wait_for_completed()
flight.land().wait_for_completed()

print('Flight ended')
drone.close()