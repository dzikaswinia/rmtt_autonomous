import logging
import command

root = logging.getLogger()
root.setLevel(logging.DEBUG)

# cmd name, coordinate index (x, y or z), factor (in- or decrease)
CMDS = [  # ["takeoff", None],
    # ["land", None],
    ["up", 2, 1],
    ["down", 2, -1],
    ["forward"],  # 1 (y) for 0 and 180°
    ["back"],  # same as forward
    ["left"],  # x if degree = 0 or 180, else y
    ["right"],  # same as left
    ["cw", 3, 1],  # rotate clockwise -> addition
    ["ccw", 3, -1]]  # subtraction


class State:
    def __init__(self, start_position):
        self.start = start_position  # (x, y, z, degrees) starting height (z) would be after take off 80-100cm
        self.pos = self.start
        logging.info(f'[state | init] Initialized a state with starting position: {start_position}')

    def update_coordinate(self, coord, val):
        if coord == 3:
            current_val = self.pos[coord]
            new_val = current_val + val
            if new_val > 360:
                new_val -= 360
                self.pos[coord] = new_val
            elif new_val < 0:
                new_val += 360
                self.pos[coord] = new_val
            else:
                self.pos[coord] += val
        else:
            self.pos[coord] += val

    def update(self, cmd, *mode):
        logging.debug(f'[state | update] Updating the position {self.pos} '
                      f'with command \"{cmd.name}\" with param {cmd.get_param()}.')
        val = None
        if cmd.name == "up" or cmd.name == "down" or cmd.name == "cw" or cmd.name == "ccw":
            val = [x for x in CMDS if x[0] == cmd.name][0]
            # print(f'val for {cmd.name} is: {val}\nself.pos[val[1]]: {self.pos[val[1]]}, val[1]: {val[1]}, val[2]: {val[2]}, cmd.param: {cmd.param}')
            self.update_coordinate(val[1], val[2] * cmd.get_param())

        if cmd.name == "forward" or cmd.name == "back":
            degree = self.pos[3]
            coordinate = 1  # y
            factor = 1
            if degree == 0 or degree == 180:
                if degree == 180:
                    factor = -1 # going down when facing down
            else:
                coordinate = 0  # x
                if degree == 270:
                    factor = -1
            if cmd.name == "back":
                factor *= -1
            self.update_coordinate(coordinate, factor * cmd.get_param())

        if cmd.name == "right" or cmd.name == "left":
            degree = self.pos[3]
            coordinate = 0  # x for 0° and 180°
            factor = 1
            if degree == 0 or degree == 180:
                if degree == 180:
                    factor = -1 # going down when facing down
            else:
                coordinate = 1  # y
                if degree == 90:
                    factor = -1
            if cmd.name == "left":
                factor *= -1
            self.update_coordinate(coordinate, factor * cmd.get_param())

        logging.debug(f'[state | update ({mode})] command: {cmd.to_string()} \t\tupdated position: {self.pos}')



# ------------------- TESTS ---------------------
"""
cmd_up = command.Command("up", 20)
cmd_cw = command.Command("cw", 90)
cmd_ccw = command.Command("ccw", 180)
cmd_ccw2 = command.Command("ccw", 90)
cmd_f = command.Command("forward", 20)
cmd_b = command.Command("back", 20)
cmd_r = command.Command("right", 20)
cmd_l = command.Command("left", 20)
state = State(start_position=[100, 100, 0, 0])
#state.update(cmd_up)
state.update(cmd_l)
state.update(cmd_cw)
state.update(cmd_l)
state.update(cmd_cw)
state.update(cmd_l)
state.update(cmd_cw)
state.update(cmd_l)
"""

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

