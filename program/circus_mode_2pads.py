import threading
import time

import config
import command
import cmd_dispatcher as cd
import drone
import position
import cmd_generator as cg


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


forward_tolerance = [10, 15, 20]
backward_tolerance = [0, 10, 15]
distance = 30
def find_circle_two_pads(drone_inst, thread, pos):
    pad = config.PAD
    print(f'pad: {pad}')
    # forward 10 cm
    cmd_f_40 = command.Command("forward", distance)
    cd.exec_cmd(drone_inst, cmd_f_40, recvThread, pos)
    time.sleep(1)
    cmd_back = command.Command("back", distance)
    cmd_cw_90 = command.Command("cw", 90)
    new_pad = config.PAD                        # string
    print(f"New pad?: {new_pad}, type: {type(new_pad)}")
    if new_pad == "2":
        print("in if part")
        for i in range(3):
            print("for loop")
            cmd_f = command.Command("forward", distance + forward_tolerance[i])
            cmd_b = command.Command("back", distance + backward_tolerance[i])
            cd.exec_cmd(drone_inst, cmd_back, thread, pos)
            cd.exec_cmd(drone_inst, cmd_cw_90, thread, pos)
            cd.exec_cmd(drone_inst, cmd_f, thread, pos)
            time.sleep(3)
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

drone_instance = drone.Drone()
recvThread = threading.Thread(target=drone_instance.recv)
recvThread.start()

def test():

    cmd_takeoff = command.Command("takeoff", None)
    cmd_cw = command.Command("cw", 90)
    cmd_f = command.Command("forward", 30)

    START = [40, 40, 80, 0]
    drone_position = position.Position(start_position=START)
    cmd_num = 10
    drone_instance.send("command")
    time.sleep(3)

    # take off
    cd.exec_cmd(drone_instance, cmd_takeoff, recvThread, drone_position)

    i = 0
    while not config.PAD_DETECTED:
        print("no pad detected yet")
        #time.sleep(2) # TODO do we need this?

        tof = cd.get_tof(drone_instance, recvThread)
        print(f'{i}\ttof: {tof} cm')

        if tof <= config.MIN_DISTANCE:
            # rotate
            print("rotating")
            cd.exec_cmd(drone_instance, cmd_cw, recvThread, drone_position)
        else:
            # forward
            cd.exec_cmd(drone_instance, cmd_f, recvThread, drone_position)
        i += 1

    print(f'PAD #2 detected: {config.PAD_DETECTED}')
    find_circle_two_pads(drone_instance, recvThread, drone_position)

    drone_instance.send("land")

# ------------------- TESTS ---------------------
