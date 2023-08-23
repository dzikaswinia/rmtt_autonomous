import logging
from copy import deepcopy
import config
import state
import command


# check if drone still in cube -> see cube limitation in config module
def is_valid_change(current_state, cmd):
    current_state_copy = deepcopy(current_state)
    current_state_copy.update(cmd)
    new_pos_wo_degrees = current_state_copy.pos[:-1]
    for i in range(len(config.POS_MAX)):
        if new_pos_wo_degrees[i] > config.POS_MAX[i]:
            logging.debug(f'[state-tracker | is_valid_param] WARNING: parameter {new_pos_wo_degrees[i]} is greater '
                  f'than valid parameter value {config.POS_MAX[i]}')
            return False
        if new_pos_wo_degrees[i] < config.POS_MIN[i]:
            logging.debug(f'[state-tracker | is_valid_param] WARNING: parameter {new_pos_wo_degrees[i]} is smaller '
                  f'than valid parameter value {config.POS_MAX[i]}.')
            return False
    logging.debug(f'[state-tracker | is_valid_param] Congratulation, you found valid command.')
    return True


# ------------------- TESTS ---------------------
"""
cmd_up = command.Command("up", 20)
cmd_f = command.Command("forward", 20)
cmd_right = command.Command("right", 40)
cmd_left = command.Command("left", 40)
state1 = state.State(start_position=[100, 100, 180, 0])
print(f'state1: {state1.pos}')
res = is_valid_change(state1, cmd_up)
print(f'The change is valid: {res}')
print(f'state1: {state1.pos}')
res = is_valid_change(state1, cmd_f)
print(f'The change is valid: {res}')
print(f'state1: {state1.pos}')
res = is_valid_change(state1, cmd_right)
print(f'The change is valid: {res}')
print(f'state1: {state1.pos}')
res = is_valid_change(state1, cmd_left)
print(f'The change is valid: {res}')
"""
