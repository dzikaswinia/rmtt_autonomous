import threading
import logging
import time
import config
import drone
import cmd_generator

root = logging.getLogger()
root.setLevel(logging.DEBUG)

CMD_LIMIT = 3

print(f'Hello in drone flying program!\n'
      f'The cube is on the size {config.MAX_X} x {config.MAX_Y}'
      f' x {config.MAX_Z} cm.\n')

drone = drone.Drone()
recvThread = threading.Thread(target=drone.recv)
recvThread.start()

cmds = [["takeoff", 8], ["forward 60", 3], ["cw 180", 2], ["land", 0]]

drone.send("command")
time.sleep(3)


# take off


for i in range(len(CMD_LIMIT)): # 2 for takeoff and land
    try:
        drone.send(cmds[i][0])
        logging.debug(f'Command send: {cmds[i][0]}')
        time.sleep(cmds[i][1])  # 2sec
    except KeyboardInterrupt:
        drone.terminate()
        recvThread.join()
        break