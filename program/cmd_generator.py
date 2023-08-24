import random as rd
import logging
import command
import config
import state
import state_tracker as st

root = logging.getLogger()
root.setLevel(logging.DEBUG)


def get_param(cmd_index):
    result = None
    logging.debug(f'[cmd_gen | get_param] Looking for the parameter for the command \"{config.CMDS[cmd_index][0]}\".')
    if config.CMDS[cmd_index][1]:
        logging.debug(f'[cmd_gen | get_param] Possible parameters {config.CMDS[cmd_index][1]}')
        param_index = rd.randint(0, len(config.CMDS[cmd_index][1]) - 1)
        result = config.CMDS[cmd_index][1][param_index]
        logging.debug(f'[cmd_gen | get_param] Choosen parameter is: {result}')
    else:
        logging.debug(f'[cmd_gen | get_param] This command does not required any parameters.')
    return result


def __generate_cmd():
    cmd_index = rd.randint(0, len(config.CMDS) - 1)
    parameter = get_param(cmd_index)
    cmd = command.Command(config.CMDS[cmd_index][0], parameter)
    logging.debug("[cmd_gen | get_cmd] Generated command \"" + cmd.name + "\" with parameter " + str(cmd.get_param()))
    return cmd


def get_valid_cmd(state):
    cmd = __generate_cmd()
    while not st.is_valid_change(state, cmd):
        cmd = __generate_cmd()
    logging.debug(f'[cmd_gen | get_valid_cmd] command: {cmd.to_string()}')
    return cmd


# ------------------- TESTS ---------------------
"""
state1 = state.State(start_position=[0, 0, 20, 0])
print(get_valid_cmd(state1))
"""


