import logging
import time
import threading
import command
import drone
import state

root = logging.getLogger()
root.setLevel(logging.DEBUG)


def exec_cmd(drone_instance, comm, receiving_thread, state):
    try:
        drone_instance.send(comm.to_string())
        state.update(comm)
        logging.info(f'[cmd_dispatcher | exec_cmd] Executed command {comm.to_string()} \t Updated position: {state.pos}')
        time.sleep(comm.get_exec_time())
    except KeyboardInterrupt:
        drone_instance.terminate()
        receiving_thread.join()


# ------------------- TESTS ---------------------

rmtt = drone.Drone()
recvThread = threading.Thread(target=rmtt.recv)
recvThread.start()

drone_state = state.State(start_position=[100, 100, 80, 0])
cmd = command.Command("back", 60)
cmd_f = command.Command("forward", 40)
cmd_r = command.Command("right", 40)
cmd_cw = command.Command("cw", 90)

rmtt.send("command")
time.sleep(3)
rmtt.send("takeoff")
time.sleep(8)

exec_cmd(rmtt, cmd_r, recvThread, drone_state)
exec_cmd(rmtt, cmd_cw, recvThread, drone_state)
rmtt.send("land")




