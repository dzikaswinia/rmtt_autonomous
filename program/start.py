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

CMD_LIMIT = 10
START = [40, 40, 80, 0]
BREAK_BETWEEN_CMD = 1 # only debugging

drone = drone.Drone()
def start():
    print(f'Hello in drone flying program!\n'
          f'\tStarting position: {START}'
          f'\n\tNumber of commands: {CMD_LIMIT}')

    #drone = drone.Drone()
    recvThread = threading.Thread(target=drone.recv)
    recvThread.start()


    drone_state = state.State(start_position=START)

    drone.send("command")
    time.sleep(3)

    # take off
    drone.send("takeoff")
    time.sleep(8)


    for i in range(CMD_LIMIT):
        print(f'[start] config.PAD_DETECTED: {config.PAD_DETECTED}')
        cmd = gen.get_valid_cmd(drone_state)
        cd.exec_cmd(drone, cmd, recvThread, drone_state)
        time.sleep(BREAK_BETWEEN_CMD)

    drone.send("land")
