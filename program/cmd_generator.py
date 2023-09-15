import random as rd
import logging
import command
import config
import position
import position_tracker as st

root = logging.getLogger()
root.setLevel(logging.DEBUG)


def get_param(cmd_index):
    result = None
    logging.debug(f'[cmd_gen | get_param] '
                  f'Looking for the parameter for the command '
                  f'\"{config.CMDS_obstacles[cmd_index][0]}\".')
    #if config.CMDS[cmd_index][1]: TODO all cmds version
    if config.CMDS_obstacles[cmd_index][1]:
        logging.debug(f'[cmd_gen | get_param] Possible parameters '
                      f'{config.CMDS_obstacles[cmd_index][1]}')
        param_index = rd.randint(0, len(config.CMDS_obstacles[cmd_index][1]) - 1)
        #result = config.CMDS[cmd_index][1][param_index] TODO all cmds version
        result = config.CMDS_obstacles[cmd_index][1][param_index]
        logging.debug(f'[cmd_gen | get_param] Chosen parameter is: {result}')
    else:
        logging.debug(f'[cmd_gen | get_param] This command does not required any parameters.')
    return result


def __generate_param(tof_value):
    max_move_len = tof_value - config.MIN_DISTANCE
    if max_move_len < 0:
        max_move_len = 0    # TODO maybe we could do something here so we do not waste time on generating command move forward by 0 cm
    if max_move_len > config.LEN_MAX:
        max_move_len = config.LEN_MAX
    param = rd.randint(config.LEN_MIN, max_move_len)
    logging.debug(f'[cmd_gen | __generate_param] param: {param}')
    return param


def __generate_cmd(tof_value):
    cmd_index = rd.randint(0, len(config.CMDS) - 1) # TODO all cmds version
    #cmd_index = rd.randint(0, len(config.CMDS_obstacles) - 1)
    # checking if parameter are for move forward
    if config.CMDS[cmd_index][0] == "forward":  #TODO all cmds version
    #if config.CMDS_obstacles[cmd_index][0] == "forward":
        parameter = __generate_param(tof_value)
        logging.debug(f'[cmd_gen | __generate_cmd] param: {parameter}')
    else:
        parameter = get_param(cmd_index)
    cmd = command.Command(config.CMDS[cmd_index][0], parameter) # TODO all cmds version
    #cmd = command.Command(config.CMDS_obstacles[cmd_index][0], parameter)
    logging.debug("[cmd_gen | --get_cmd] Generated command \"" + cmd.name
                  + "\" with parameter " + str(cmd.get_param()))
    return cmd


def get_valid_cmd(position, tof_value):
    cmd = __generate_cmd(tof_value)
    while not st.is_valid_change(position, cmd):
        cmd = __generate_cmd(tof_value)
    logging.debug(f'[cmd_gen | get_valid_cmd] command: {cmd.to_string()}')
    return cmd


def generate_forward_cmd(tof_value):
    parameter = __generate_param(tof_value)
    cmd = command.Command("forward", parameter)
    return cmd


def get_valid_forward_cmd(position, tof_value):
    cmd = generate_forward_cmd(tof_value)
    while not st.is_valid_change(position, cmd):
        cmd = generate_forward_cmd(tof_value)
    logging.info(f'[cmd_gen | get_valid_cmd] command: {cmd.to_string()}')
    return cmd


# ------------- circus mode ---------------------------------------------------------------
def get_circus_cmd(position):
    """
    only forward, cw and ccw cmds
    :param tof_value:
    :return:
    """
    logging.info(f'[cmd_gen | get_circus_cmd] trieggered')
    cmd = __generate_circus_cmd()
    while not st.is_valid_change(position, cmd):
        cmd = __generate_circus_cmd()
    logging.debug(f'[cmd_gen | get_circus_cmd] command: {cmd.to_string()}')
    return cmd


def __generate_circus_cmd():
    cmd_index = rd.randint(0, len(config.CMDS_obstacles) - 1)
    logging.info(f'[cmd_gen | generate_circus_cmd] trieggered with cmd index: {cmd_index}')
    parameter = get_param(cmd_index)
    cmd = command.Command(config.CMDS_obstacles[cmd_index][0], parameter)
    logging.debug("[cmd_gen | circus mode] Generated command \"" + cmd.name
                  + "\" with parameter " + str(cmd.get_param()))
    return cmd

"""
def get_param_limited(cmd_index):
    result = None
    logging.debug(f'[cmd_gen | get_param] '
                  f'Looking for the parameter for the command \"{config.CMDS_obstacles[cmd_index][0]}\".')
    #if config.CMDS[cmd_index][1]: TODO all cmds version
    if config.CMDS_obstacles[cmd_index][1]:
        logging.debug(f'[cmd_gen | get_param] Possible parameters {config.CMDS_obstacles[cmd_index][1]}')
        param_index = rd.randint(0, len(config.CMDS_obstacles[cmd_index][1]) - 1)
        #result = config.CMDS[cmd_index][1][param_index] TODO all cmds version
        result = config.CMDS_obstacles[cmd_index][1][param_index]
        logging.debug(f'[cmd_gen | get_param] Chosen parameter is: {result}')
    else:
        logging.debug(f'[cmd_gen | get_param] This command does not required any parameters.')
    return result



"""

# ------------------- TESTS ---------------------
"""
tof = 80
pos = position.Position(start_position=[0, 0, 20, 0])
print(get_valid_cmd(pos, tof).to_string())

"""





