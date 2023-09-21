import threading
import time

import config
import command
import cmd_dispatcher as cd
import drone
import position
import cmd_generator as cg

# TODO maybe we can delete this
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
    cmd_f_40 = command.Command("forward", config.DIST_BETWEEN_PADS)
    cd.exec_cmd(drone_inst, cmd_f_40, recvThread, pos)
    time.sleep(1)
    cmd_back = command.Command("back", config.DIST_BETWEEN_PADS)
    cmd_cw_90 = command.Command("cw", 90)
    new_pad = config.PAD                        # string
    print(f"New pad?: {new_pad}, type: {type(new_pad)}")
    if new_pad == "2":
        print("in if part")
        for i in range(3):
            print("for loop")
            cmd_f = command.Command("forward", config.DIST_BETWEEN_PADS + config.TOLERANCE_FORWARD[i])
            cmd_b = command.Command("back", config.DIST_BETWEEN_PADS + config.TOLERANCE_BACKWARD[i])
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


def get_reverse_cmd(cmd):
    return config.REVERSE_CMD_NAMES[cmd]



# ------------ centering above the mission pad --------------------
def get_correction_x_axis(x, drone_position):
    pos = drone_position.pos
    drone_orientation = pos[3]    # north = 0°, east = 90° etc
    cmd_name = ""
    if x > 0:
        # positive <---
        if drone_orientation == 90 or drone_orientation == 270:
            cmd_name = "back"
            if drone_orientation == 270:
                cmd_name = "forward"
        else:
            cmd_name = "left"
            if drone_orientation == 180:
                cmd_name = "right"
    else:
        # negative -->
        if drone_orientation == 90 or drone_orientation == 270:
            cmd_name = "forward"
            if drone_orientation == 270:
                cmd_name = "back"
        else:
            cmd_name = "right"
            if drone_orientation == 180:
                cmd_name = "left"

    # smallest possible parameter is anyway 20cm
    if abs(x) < 20:
        print(f'x parameter smaller than 20')
        cmd_2 = command.Command(cmd_name, 20 + abs(x) + config.CEN_COR_VAL, "free_mode")
        rev_cmd_name = config.REVERSE_CMD_NAMES[cmd_name]
        cmd_1 = command.Command(rev_cmd_name, 20, "free_mode")
        print(f'cmd 1 {cmd_1.to_string()}, cmd 2: {cmd_2.to_string()}')
        return [cmd_1, cmd_2]

    else:
        parameter = abs(x)
        cmd_1 = command.Command(cmd_name, parameter + config.CEN_COR_VAL, "free_mode")
        return [cmd_1]



def get_correction_y_axis(y, drone_position):
    pos = drone_position.pos
    drone_orientation = pos[3]    # north = 0°, east = 90° etc
    cmd_name = ""
    factor = 1
    if y > 0:
        # positive - move down
        if drone_orientation == 90 or drone_orientation == 270:
            cmd_name = "right"
            if drone_orientation == 270:
                cmd_name = "left"
        else:
            cmd_name = "back"
            if drone_orientation == 180:
                cmd_name = "forward"
    else:
        # negative . move up
        if drone_orientation == 90 or drone_orientation == 270:
            cmd_name = "left"
            if drone_orientation == 270:
                cmd_name = "right"
        else:
            cmd_name = "forward"
            if drone_orientation == 180:
                cmd_name = "back"

    # smallest possible parameter is anyway 20cm
    if abs(y) < 20:
        print(f'y parameter smaller than 20')
        cmd_2 = command.Command(cmd_name, 20 + abs(y) + config.CEN_COR_VAL, "free_mode")
        rev_cmd_name = config.REVERSE_CMD_NAMES[cmd_name]
        cmd_1 = command.Command(rev_cmd_name, 20, "free_mode")
        print(f'cmd 1 {cmd_1.to_string()}, cmd 2: {cmd_2.to_string()}')
        return [cmd_1, cmd_2]

    else:
        parameter = abs(y)
        cmd_1 = command.Command(cmd_name, parameter + config.CEN_COR_VAL, "free_mode")
        return [cmd_1]
    """
    parameter = abs(y)
    if abs(y) < 21:
        parameter = 20
    return command.Command(cmd_name, parameter + config.CEN_COR_VAL, "free_mode")
    """



def center(pos):
    print("--- center ----")
    x = config.CURRENT_X
    y = config.CURRENT_Y

    threshold = config.THRESHOLD
    print(f"Centring: current x: {x}, current y {y}, type {type(x)}")
    result = []
    change_x = False
    change_y = False
    if x > threshold or x < (threshold * -1):
        change_x = True
    if y > threshold or y < (threshold * -1):
        change_y = True

    if change_x:
        cmds = get_correction_x_axis(x, pos)
        for cmd in cmds:
            result.append(cmd)
    if change_y:
        cmds = get_correction_y_axis(y, pos)
        for cmd in cmds:
            result.append(cmd)
    print(f'result: {result}')
    return result


def get_direction(position):
    pos = position.pos
    drone_orient = pos[3]
    print(f'drone orientation {drone_orient}')
    direction = "n"
    if drone_orient == 270:
        direction = "w"
    if drone_orient == 90:
        direction = "e"
    print(f'### DIREXCTION:direction is {direction}')
    return direction



# ----------- main method -----------------------------------------------
def test():
    cmd_takeoff = command.Command("takeoff", None)
    cmd_cw = command.Command("cw", 90)
    cmd_f = command.Command("forward", 30)

    START = [40, 20, 80, 270]  # TODO set degree
    drone_position = position.Position(start_position=START)
    cmd_num = 10
    drone_instance.send("command")
    time.sleep(3)

    # take off
    cd.exec_cmd(drone_instance, cmd_takeoff, recvThread, drone_position)

    i = 0
    while not config.PAD_DETECTED:
        print("no pad detected yet")
        time.sleep(2) # TODO do we need this?

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

    print(f'PAD detected: {config.PAD_DETECTED}, \n'
          f'x: {config.CURRENT_X}, y: {config.CURRENT_Y}')
    time.sleep(4) # pause to let sensor send right data
    print(f'x: {config.CURRENT_X}, y: {config.CURRENT_Y}')

    print(f'Is the pad still detected?: {config.PAD_DETECTED}')
    if config.PAD_DETECTED:
        cmds = center(drone_position)
        print(f"we have {len(cmds)} correcting commands")
        for cmd in cmds:
            print(f'CMD: {cmd.to_string()}')
            cd.exec_cmd(drone_instance, cmd, recvThread, drone_position)
        #find_circle_two_pads(drone_instance, recvThread, drone_position)
    else:
        print("pad not detected, continue flying")
    


    #cmd_f20 = command.Command("forward", 20)
    #cd.exec_cmd(drone_instance, cmd_f20, recvThread, drone_position)
    #time.sleep(2)
    direction = get_direction(drone_position)
    #cmd_b20 = command.Command("back", 20)
    #cd.exec_cmd(drone_instance, cmd_b20, recvThread, drone_position)
    if direction != "n":
        rota_cmd_name = "ccw"
        if direction == "w":
            rota_cmd_name = "cw"

        rotation_cmd = command.Command(rota_cmd_name, 90)
        cd.exec_cmd(drone_instance, rotation_cmd, recvThread, drone_position)

    # center again
    cmds = center(drone_position)
    print(f"we have {len(cmds)} correcting commands")
    for cmd in cmds:
        print(f'CMD: {cmd.to_string()}')
        cd.exec_cmd(drone_instance, cmd, recvThread, drone_position)

    # adjusting height
    drone_instance.send("up 20")
    time.sleep(1)
    drone_instance.send("down 25")
    time.sleep(1)

    # fly through
    drone_instance.send("forward 60")

    drone_instance.send("land")


# --------- setup ----------------------------------------------------
drone_instance = drone.Drone()
recvThread = threading.Thread(target=drone_instance.recv)
recvThread.start()

# ------------------- TESTS ---------------------
"""
drone_pos = position.Position([40, 40, 80, 0])
cmds = center(drone_pos)
for cmd in cmds:
    print(f'command : {cmd.to_string()}')

"""


