import threading
import logging
import time

import config
import drone
import state
import cmd_generator as gen
import cmd_dispatcher as cd
import command


root = logging.getLogger()
root.setLevel(logging.INFO)

CMD_LIMIT = 4
START = [40, 40, 80, 0]
BREAK_BETWEEN_CMD = 3 # only debugging

TOF = [10000, 50, 120, 25] # TODO loe

drone = drone.Drone()
def start():
    print(f'Hello in drone flying program!\n'
          f'\tStarting position: {START}'
          f'\n\tNumber of commands: {CMD_LIMIT}')

    recvThread = threading.Thread(target=drone.recv)
    recvThread.start()

    drone_state = state.State(start_position=START)

    drone.send("command")
    time.sleep(3)

    # take off
    drone.send("takeoff") # TODO wait for ok before preceding
    time.sleep(15)
    i = 0
    for i in range(CMD_LIMIT):
        #tof = TOF[i]
        print(f'[start] config.PAD_DETECTED: {config.PAD_DETECTED}')
        if config.PAD_DETECTED:
            drone.send("land")
            break
        else:
            tof = cd.get_tof(drone, recvThread)

            if tof <= config.MIN_DISTANCE:
                # rotate
                print("object infront detected - rotation")
                cmd = command.Command("cw", 90) # TODO change to random cmd?
                cd.exec_cmd(drone, cmd, recvThread, drone_state)
            else:
                print("no object detected - forward")
                cmd = gen.get_valid_forward_cmd(drone_state, tof)
                cd.exec_cmd(drone, cmd, recvThread, drone_state)
                #time.sleep(BREAK_BETWEEN_CMD) # TODO only for debugging
        i += 1

    drone.send("land")


# ------------------- TESTS ---------------------
start()
