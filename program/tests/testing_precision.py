import threading
import time

import drone
import command
import cmd_dispatcher as cd
import position

# setup
cmd_to = command.Command("takeoff", None)
cmd_f = command.Command("forward", 70)
cmd_r = command.Command("right", 60)

drone_instance = drone.Drone()
recvThread = threading.Thread(target=drone_instance.recv)
recvThread.start()

START = [0, 0, 80, 0]
drone_position = position.Position(start_position=START)

drone_instance.send("command")
drone_instance.send("takeoff")
time.sleep(8)
cd.exec_cmd(drone_instance, cmd_f, recvThread, drone_position)
time.sleep(3)
drone_instance.send("right 60")
time.sleep(3)
drone_instance.send("land")
