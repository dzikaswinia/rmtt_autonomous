import threading
import time

import config
import command
import cmd_dispatcher as cd
import drone
import position


def find_circle_one_pad(drone_inst, thread, pos):
    prev_x = config.CURRENT_X
    print(f'x: {prev_x}, current x: {config.CURRENT_X}')
    # forward 10 cm
    cmd_f_20 = command.Command("forward", 20)
    cd.exec_cmd(drone_inst, cmd_f_20, recvThread, pos)
    current_x = config.CURRENT_X - 4
    print(f"prev: {prev_x} and current: {current_x}")
    if prev_x < current_x:
        print("right direction")
    else:
        print("else")
        cmd_cw_180 = command.Command("cw", 180)
        cmd_cw_90 = command.Command("cw", 90)
        for i in range(3):
            print("for loop")
            current_x = config.CURRENT_X - 4
            cd.exec_cmd(drone_inst, cmd_cw_180, thread, pos)
            cd.exec_cmd(drone_inst, cmd_f_20, thread, pos)
            cd.exec_cmd(drone_inst, cmd_cw_90, thread, pos)
            if prev_x < current_x:
                print("right direction")
                break


def find_circle_two_pads(drone_inst, thread, pos):
    pad = config.PAD
    print(f'pad: {pad}')
    # forward 10 cm
    cmd_f_20 = command.Command("forward", 40)
    cd.exec_cmd(drone_inst, cmd_f_20, recvThread, pos)
    time.sleep(1)
    new_pad = config.PAD                        # string
    print(f"New pad?: {new_pad}")
    if new_pad == "2":
        cmd_cw_180 = command.Command("cw", 180)
        cmd_cw_90 = command.Command("cw", 90)
        for i in range(3):
            print("for loop")
            cd.exec_cmd(drone_inst, cmd_cw_180, thread, pos)
            cd.exec_cmd(drone_inst, cmd_f_20, thread, pos)
            cd.exec_cmd(drone_inst, cmd_cw_90, thread, pos)
            cd.exec_cmd(drone_inst, cmd_f_20, thread, pos)
            time.sleep(1)
            new_pad = config.PAD  # string
            print(f"New pad?: {new_pad}")
            if new_pad == "1":
                print("right direction")
                break
            else:
                print("wrong direction")
                continue
    else:
        print("right direction")

    """
        if prev_x < current_x:
        print("right direction")
    else:
        print("else")
        cmd_cw_180 = command.Command("cw", 180)
        cmd_cw_90 = command.Command("cw", 90)
        for i in range(3):
            print("for loop")
            current_x = config.CURRENT_X - 4
            cd.exec_cmd(drone_inst, cmd_cw_180, thread, pos)
            cd.exec_cmd(drone_inst, cmd_f_20, thread, pos)
            cd.exec_cmd(drone_inst, cmd_cw_90, thread, pos)
            if prev_x < current_x:
                print("right direction")
                break
    """



drone_instance = drone.Drone()
cmd_takeoff = command.Command("takeoff", None)
recvThread = threading.Thread(target=drone_instance.recv)
recvThread.start()

START = [40, 40, 80, 0]
drone_position = position.Position(start_position=START)


def test():
    drone_instance.send("command")
    time.sleep(3)

    # take off
    cd.exec_cmd(drone_instance, cmd_takeoff, recvThread, drone_position)

    while not config.PAD_DETECTED:
        print("no pad detected yet")
        time.sleep(2)

    find_circle_two_pads(drone_instance, recvThread, drone_position)

    drone_instance.send("land")

# ------------------- TESTS ---------------------
