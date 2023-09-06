
# cube limitations (in cm)
POS_MAX = [80, 80, 180]
POS_MIN = [0, 0, 20]

# websocket for SDK cmd
CMD_IP = '192.168.10.1'
CMD_PORT = 8889
HOST_IP = '0.0.0.0'
RESP_PORT = 9000

# cmd
TAKEOFF_EXEC_TIME = 8
MOVE_EXEC_TIME = 4
ROTATION_EXEC_TIME = 3
MOVE = [40, 60, 80, 100, 120]
MOVE_UP_DOWN = [60, 80, 120]
DEGREES = [90, 180]
CMDS = [#["takeoff", None],
        #["land", None],
       # ["up", MOVE_UP_DOWN, MOVE_EXEC_TIME],
        #["down", MOVE_UP_DOWN, MOVE_EXEC_TIME],
        ["forward", MOVE, MOVE_EXEC_TIME],
        ["back", MOVE, MOVE_EXEC_TIME],
        ["left", MOVE, MOVE_EXEC_TIME],
        ["right", MOVE, MOVE_EXEC_TIME],
        ["cw", DEGREES, ROTATION_EXEC_TIME],    # rotate clockwise
        ["ccw", DEGREES, ROTATION_EXEC_TIME]   # rotate counter-clockwise
        ]

# mission pad detected (not constant)
PAD_DETECTED = False
