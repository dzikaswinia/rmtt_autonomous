import logging
import time
import threading
import command
import drone

root = logging.getLogger()
root.setLevel(logging.DEBUG)

def exec_cmd(drone, cmd, receiving_thread):
    try:
        print(cmd.to_string())
        drone.send(cmd.to_string())
        exec_time = cmd.get_exec_time()
        logging.debug(f'Cmd "{cmd.name} with exec time {exec_time}')
        time.sleep(cmd.get_exec_time())  # 2sec
    except KeyboardInterrupt:
        drone.terminate()
        receiving_thread.join()

# ------------------- TESTS ---------------------

drone = drone.Drone()
recvThread = threading.Thread(target=drone.recv)
recvThread.start()

cmd = command.Command("back", 60)
cmd_f = command.Command("forward", 40)
cmd_r = command.Command("right", 20)

drone.send("command")
time.sleep(3)
drone.send("takeoff")
time.sleep(8)

exec_cmd(drone, cmd, recvThread)
