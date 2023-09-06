import threading
import logging
import time
import config
import drone
import state
import cmd_generator as gen
import cmd_dispatcher as cd

root = logging.getLogger()
root.setLevel(logging.INFO)

CMD_LIMIT = 20
START = [80, 80, 80, 0]

print(f'Hello in drone flying program!\n'
      f'The cube is on the size {config.POS_MAX} cm.\n'
      f'\tStarting position: {START}'
      f'\n\tNumber of commands: {CMD_LIMIT}')

drone = drone.Drone()
recvThread = threading.Thread(target=drone.recv)
recvThread.start()

#cmds = [["takeoff", 8], ["forward 60", 3], ["cw 180", 2], ["land", 0]]

drone_state = state.State(start_position=START)

drone.send("command")
time.sleep(3)

# take off
drone.send("takeoff")
time.sleep(8)


for i in range(CMD_LIMIT):
    cmd = gen.get_valid_cmd(drone_state)
    cd.exec_cmd(drone, cmd, recvThread, drone_state)

drone.send("land")
