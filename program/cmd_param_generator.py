import random as rd
import logging

root = logging.getLogger()
root.setLevel(logging.DEBUG)

CMDS = [#["takeoff", None],
        #["land", None],
        ["up", [20]],
        ["down", [20]],
        ["forward", [20, 40, 60]],
        ["back", [20, 40, 60]],
        ["left", [20, 40, 60]],
        ["right", [20, 40, 60]],
        ["cw", [90, 180]],    # rotate clockwise
        ["ccw", [90, 180]]]   # rotate counter-clockwise


class command:
    def __init__(self, name, param):
        self.name = name
        self.param = param


def get_param(cmd_index):
    result = None
    logging.debug(f'[cmd_param_gen | get_param] Looking for the parameter for the command \"{CMDS[cmd_index][0]}\".')
    if (CMDS[cmd_index][1]):
        logging.debug(f'[cmd_param_gen | get_param] Possible parameters {CMDS[cmd_index][1]}')
        param_index = rd.randint(0, len(CMDS[cmd_index][1]) - 1)
        result = CMDS[cmd_index][1][param_index]
        logging.debug(f'[cmd_param_gen | get_param] Choosen parameter is: {result}')
    else:
        logging.debug(f'[cmd_param_gen | get_param] This command does not required any parameters.')
    return result


def get_cmd():
    cmd_index = rd.randint(0, len(CMDS) - 1)
    parameter = get_param(cmd_index)
    cmd = command(CMDS[cmd_index][0], param=parameter)
    logging.debug("[cmd_param_gen | get_cmd] Generated command \"" + cmd.name + "\" with parameter " + str(cmd.param))


get_cmd()

