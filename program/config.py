
# cube limitations (in cm)
MAX_Y = 200
MAX_X = 200
MAX_Z = 180
POS_MAX = [200, 200, 180]
POS_MIN = [0, 0, 20]

# websocket for SDK cmd
CMD_IP = '192.168.10.1'
CMD_PORT = 8889
HOST_IP = '0.0.0.0'
RESP_PORT = 9000

# cmd
TAKEOFF_EXEC_TIME = 8
MOVE_EXEC_TIME = 3
ROTATION_EXEC_TIME = 2
MOVE = [40, 60, 100, 120]
MOVE_UP_DOWN = [20, 50, 80, 120]
CMDS = [#["takeoff", None],
        #["land", None],
        ["up", MOVE_UP_DOWN, MOVE_EXEC_TIME],
        ["down", MOVE_UP_DOWN, MOVE_EXEC_TIME],
        ["forward", MOVE, MOVE_EXEC_TIME],
        ["back", MOVE, MOVE_EXEC_TIME],
        ["left", MOVE, MOVE_EXEC_TIME],
        ["right", MOVE, MOVE_EXEC_TIME],
        ["cw", MOVE, ROTATION_EXEC_TIME],    # rotate clockwise
        ["ccw", MOVE, ROTATION_EXEC_TIME]]   # rotate counter-clockwise