import threading
import logging
import time
import config
import drone
import cmd_generator

root = logging.getLogger()
root.setLevel(logging.DEBUG)

TIME_LIMIT = 10 # sec

print(f'Hello in drone flying program!\n'
      f'The cube is on the size {config.MAX_X} x {config.MAX_Y}'
      f' x {config.MAX_Z} cm.\n')

drone = drone.Drone()
recvThread = threading.Thread(target=drone.recv)
recvThread.start()

cmds = ["takeoff", "forward 20", "cw 90", "land"]

drone.send("command")
time.sleep(3)

for i in range(len(cmds)):
    try:
        drone.send(cmds[i])
        logging.debug(f'Command send: {cmds[i]}')
        time.sleep(2)  # 2sec
    except KeyboardInterrupt:
        drone.terminate()
        recvThread.join()
        break