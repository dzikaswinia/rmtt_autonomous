import logging
import unittest
import command

root = logging.getLogger()
root.setLevel(logging.DEBUG)

CMDS = [  # ["takeoff", None],
    # ["land", None],
    ["up", 2, 1],
    ["down", 2, -1],
    ["forward", None],  # if degree = 0 v degree = 180 -> y, if degree = 90 v degree = 270 -> x
    ["back", None],  # same as forward
    ["left", None],  # x if degree = 0 or 180, else y
    ["right", None],  # same as left
    ["cw", 3, 1],  # rotate clockwise -> addition
    ["ccw", 3, -1]]  # subtraction


class State:
    def __init__(self, start_position):
        self.start = start_position  # (x, y, z, degrees) starting height (z) would be after take off 80-100cm
        self.pos = self.start
        # logging.DEBUG(f'[state_tracker | init] Initialazed a state with starting position: {start_position}')
        print(f'[state_tracker | init] Initialized a state with starting position: {start_position}')

    # position during flight and height could be calculated by tracking the changes in respect to the starting position
    # It would be pretty straight forward (no obstacles in flight field) but when we want to allow the cmd "rotate"
    # thing starting to get complicated (geometry is needed)

    def update_coordinate(self, coord, val):
        if (coord == 3):
            current_val = self.pos[coord]
            new_val = current_val + val
            if (new_val > 360):
                new_val -= 360
                self.pos[coord] = new_val
            elif (new_val < 0):
                new_val += 360
                self.pos[coord] = new_val
            else:
                self.pos[coord] += val
        else:
            self.pos[coord] += val

    def update(self, cmd):
        print(f'[state_tracker | update] Updating the position with command: {cmd.name} with param: {cmd.param}'
              f'\nCurrent position: {self.pos}.')
        val = None
        if cmd.name == "up" or cmd.name == "down" or cmd.name == "cw" or cmd.name == "ccw":
            val = [x for x in CMDS if x[0] == cmd.name][0]
            # print(f'val for {cmd.name} is: {val}\nself.pos[val[1]]: {self.pos[val[1]]}, val[1]: {val[1]}, val[2]: {val[2]}, cmd.param: {cmd.param}')
            self.update_coordinate(val[1], val[2] * cmd.param)
            # self.pos[val[1]] += val[2] * cmd.param

        if cmd.name == "forward":
            degree = self.pos[3]
            coordinate = None
            factor = 1
            if degree == 0 or degree == 180:
                coordinate = 1  # y
                if degree == 180:
                    factor = -1 # going down when facing down

            else:
                coordinate = 0  # x
                if degree == 270:
                    factor = -1
            self.update_coordinate(coordinate, factor * cmd.param)

        print(f'Changed position: {self.pos}')


cmd_up = command.Command("up", 22)
cmd_cw = command.Command("cw", 90)
cmd_ccw = command.Command("ccw", 180)
cmd_ccw2 = command.Command("ccw", 90)
cmd_f = command.Command("forward", 40)
state = State(start_position=[100, 100, 0, 270])
state.update(cmd_up)
state.update(cmd_f)


""" testing rotation 
state.update(cmd_cw)
state.update(cmd_cw)
state.update(cmd_cw)
state.update(cmd_cw)
state.update(cmd_cw)
state.update(cmd_ccw)
state.update(cmd_ccw)
state.update(cmd_ccw2)
"""

