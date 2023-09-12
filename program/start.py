import threading
import logging
import time

import config
import drone
import position
import cmd_generator as gen
import cmd_dispatcher as cd
import command

root = logging.getLogger()
root.setLevel(logging.INFO)

CMD_LIMIT = 4
START = [40, 40, 80, 0]
cmd_num = 20
BREAK_BETWEEN_CMD = 3 # only debugging  # TODO loe


# setup
drone = drone.Drone()
cmd_takeoff = command.Command("takeoff", None)
cmd_cw = command.Command("cw", 90)
cmd_f = command.Command("forward", 30)


def start():
    print(f'Hello in drone flying program!\n'
          f'\tStarting position: {START}'
          f'\n\tNumber of commands: {CMD_LIMIT}')

    recvThread = threading.Thread(target=drone.recv)
    recvThread.start()

    drone_position = position.Position(start_position=START)

    drone.send("command")
    time.sleep(3)

    # take off
    cd.exec_cmd(drone, cmd_takeoff, recvThread, drone_position)

    i = 0
    for i in range(cmd_num):
        tof = cd.get_tof(drone, recvThread)
        print(f'{i}\ttof: {tof} cm')

        if config.PAD_DETECTED:
            drone.send("land")
            break
        else:
            if tof <= config.MIN_DISTANCE:
                # rotate
                cd.exec_cmd(drone, cmd_cw, recvThread, drone_position)
            else:
                # forward
                cd.exec_cmd(drone, cmd_f, recvThread, drone_position)
        i += 1

    drone.send("land")


# ------------------- TESTS ---------------------
#start()
