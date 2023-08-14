import random as rd
import logging

root = logging.getLogger()
root.setLevel(logging.DEBUG)

CMDS = [["takeoff", None],
        ["land", None],
        ["up", "cm"],
        ["down", "cm"],
        ["forward", "cm"],
        ["back", "cm"],
        ["left", "cm"],
        ["right", "cm"],
        ["cw", "degrees"],    # rotate clockwise
        ["ccw", "degrees"]]   # rotate counter-clockwise


class command:
    def __init__(self, name, param):
        self.name = name
        self.param = param


def get_param(cmd_name, oaram_type):
    result = 0

    return result


def get_cmd():
    cmd_index = rd.randint(0, len(CMDS) - 1)
    parameter = 0
    cmd = command(CMDS[cmd_index][0], param=parameter)
    print(str(cmd_index))
    logging.debug("[cmd_param_gen | get_cmd] Generated command \"" + cmd.name + "\" with parameter " + str(cmd.param))


get_cmd()

