import random as rd
import logging
import command
import config

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


def get_cmd():
    cmd_index = rd.randint(0, len(config.CMDS) - 1)
    parameter = get_param(cmd_index)
    cmd = command.Command(config.CMDS[cmd_index][0], parameter)
    logging.debug("[cmd_gen | get_cmd] Generated command \"" + cmd.name + "\" with parameter " + str(cmd.get_param()))


# ------------------- TESTS ---------------------
get_cmd()

