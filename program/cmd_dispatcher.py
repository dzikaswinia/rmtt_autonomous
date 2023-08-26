import logging
import time
import threading
import command
import drone
import state

root = logging.getLogger()
root.setLevel(logging.INFO)


def exec_cmd(drone_instance, comm, receiving_thread, state):
    try:
        state.update(comm)
        response = drone_instance.send(comm.to_string())
        time.sleep(comm.get_exec_time())
        logging.info(f'here is drone exec state: {drone_instance.exec_state}')
        if drone_instance.exec_state == 'ok':
            #state.update(comm)
            logging.info(f'[cmd_dispatcher | exec_cmd] Executed command {comm.to_string()} '
                         f'\t Updated position: {state.pos}')
        else:
            # undo the update
            state.undo()
            logging.info(f'[cmd_dispatcher | exec_cmd] Command {comm.to_string()} have not been'
                         f' executed. Current position: {state.pos}')

    except KeyboardInterrupt:
        drone_instance.terminate()
        receiving_thread.join()


# ------------------- TESTS ---------------------
"""
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

exec_cmd(rmtt, cmd_f, recvThread, drone_state)
exec_cmd(rmtt, cmd_cw, recvThread, drone_state)
rmtt.send("land")

"""







