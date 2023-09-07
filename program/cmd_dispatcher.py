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
        logging.info(f'here is drone response: {drone_instance.exec_state}')
        if drone_instance.exec_state == 'ok':
            state.update(comm)
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


def exec_sensor_cmd(drone_instance, comm, receiving_thread):
    try:
        #state.update(comm)
        drone_instance.send(comm)
        response = drone_instance.recv()
        #time.sleep(comm.get_exec_time())

        logging.info(f'sensor data: #{response}#')
        return response
    except KeyboardInterrupt:
        drone_instance.terminate()
        receiving_thread.join()


def get_real_response(drone_instance):
    is_tof_resp = False
    response = ""
    while not is_tof_resp:
        response = drone_instance.recv()
        logging.debug(f'trying to get tof response: {response}')
        print()
        if response.startswith("tof"):
            is_tof_resp = True

        if response == "out of range":
            response = "tof 9000"
            is_tof_resp = True

    return response


def get_tof(drone_instance, receiving_thread):
    """
    Gets tof sensor data (mm) and converts it to cm with rounding up.

    :param drone_instance: drone
    :param receiving_thread: thread
    :return: distance in cm as integer
    """
    try:
        drone_instance.send("EXT tof?")
        response = get_real_response(drone_instance)
        logging.info(f'sensor data: {response}')

        # extracting value
        values = response.split(" ")
        tof_mm = int(values[1])

        # converting from mm to cm (as integer)
        tof_cm = round(tof_mm * 0.1)
        return tof_cm
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







