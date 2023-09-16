import logging
import time
import threading
import command
import drone
import position

root = logging.getLogger()
root.setLevel(logging.INFO)


def exec_cmd(drone_instance, comm, receiving_thread, pos):
    print("exec cmd")
    try:
        logging.info(f'[cmd_dispatcher | exec_cmd] trying execute cmd {comm.name}')
        pos.update(comm)
        drone_instance.send(comm.to_string())
        is_move_resp = False
        while not is_move_resp:
            response = drone_instance.recv()
            logging.info(f'[cmd_dispatcher | exec_cmd] trying to get move cmd response: {response}')
            if response.startswith("ok"):
                is_move_resp = True

            else:
                logging.info(f"[cmd_dispatcher | exec_cmd] exec move cmd else !!! {response}")
                is_move_resp = True
        logging.info(f"[cmd_dispatcher | exec_cmd] cmd executed")

    except KeyboardInterrupt:
        drone_instance.terminate()
        receiving_thread.join()


def exec_sensor_cmd(drone_instance, comm, receiving_thread):
    try:
        #state.update(comm)
        drone_instance.send(comm)
        logging.info(f'[cmd_dispatcher | exec_sensor_cmd] drone exec state: {drone_instance.exec_state}')
        response = drone_instance.recv()
        logging.info(f'[cmd_dispatcher | exec_sensor_cmd] response: {response}')
        return response
    except KeyboardInterrupt:
        drone_instance.terminate()
        receiving_thread.join()


def get_real_response(drone_instance):
    is_tof_resp = False
    response = ""
    while not is_tof_resp:
        response = drone_instance.recv()
        logging.debug(f'### trying to get tof response: {response}')
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
        print("get tof")
        drone_instance.send("EXT tof?")
        response = get_real_response(drone_instance)
        logging.info(f'[command_dispatcher | get_tof] sensor data: {response}')

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

drone_pos = position.Position(start_position=[40, 40, 80, 0])
#cmd = command.Command("back", 60)
cmd_f = command.Command("forward", 40)
#cmd_r = command.Command("right", 40)
cmd_cw = command.Command("cw", 90)

rmtt.send("command")
time.sleep(3)
#rmtt.send("takeoff")
cmd_takeoff = command.Command("takeoff", None)
exec_cmd(rmtt, cmd_takeoff, recvThread, drone_pos)
time.sleep(8)

exec_cmd(rmtt, cmd_f, recvThread, drone_pos)
exec_cmd(rmtt, cmd_cw, recvThread, drone_pos)
rmtt.send("land")


"""










