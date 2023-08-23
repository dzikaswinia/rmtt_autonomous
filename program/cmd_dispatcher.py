import logging
import time
import threading
import command
import drone

root = logging.getLogger()
root.setLevel(logging.DEBUG)


def exec_cmd(drone_instance, comm, receiving_thread):
    try:
        drone_instance.send(comm.to_string())
        exec_time = comm.get_exec_time()
        logging.debug(f'Cmd \"{comm.name}\" with exec time {exec_time}')
        time.sleep(comm.get_exec_time())
    except KeyboardInterrupt:
        drone_instance.terminate()
        receiving_thread.join()


# ------------------- TESTS ---------------------
"""
rmtt = drone.Drone()
recvThread = threading.Thread(target=rmtt.recv)
recvThread.start()

cmd = command.Command("back", 60)
cmd_f = command.Command("forward", 40)
cmd_r = command.Command("right", 20)
cmd_cw = command.Command("cw", 90)

rmtt.send("command")
time.sleep(3)
rmtt.send("takeoff")
time.sleep(8)

exec_cmd(rmtt, cmd_r, recvThread)
exec_cmd(rmtt, cmd_cw, recvThread)
rmtt.send("land")
"""

