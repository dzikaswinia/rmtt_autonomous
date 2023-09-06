import time

from djitellopy import Tello

print("setup")
tello = Tello()
tello.connect()

for i in range(0, 100000):
    print(i)
    print(f'pad: {tello.get_mission_pad_id()}')


