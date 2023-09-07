
# -------- cube limitations ----------------------------
POS_MAX = [80, 80, 180]         # cm
POS_MIN = [0, 0, 20]            # cm
MIN_DISTANCE = 50               # cm

# --------- websocket for SDK cmd ----------------------
CMD_IP = '192.168.10.1'
CMD_PORT = 8889
HOST_IP = '0.0.0.0'
RESP_PORT = 9000

# --------- COMMANDS ------------------------------------
# command execution time
TAKEOFF_EXEC_TIME = 8
MOVE_EXEC_TIME = 4
ROTATION_EXEC_TIME = 3
# move length
LEN_MIN = 0             # cm   TODO what if generated move length is smaller that this?
LEN_MAX = 100           # cm
MOVE = [40, 60, 80, 100]        # cm
MOVE_UP_DOWN = [60, 80, 120]    # cm
DEGREES = [90, 180]        # degrees  TODO extend with 270° but will position tracking still work?
CMDS = [#["takeoff", None],
        #["land", None],
       # ["up", MOVE_UP_DOWN, MOVE_EXEC_TIME],
        #["down", MOVE_UP_DOWN, MOVE_EXEC_TIME],
        ["forward", MOVE, MOVE_EXEC_TIME],
        #["back", MOVE, MOVE_EXEC_TIME],
        #["left", MOVE, MOVE_EXEC_TIME],
        #["right", MOVE, MOVE_EXEC_TIME],
        ["cw", DEGREES, ROTATION_EXEC_TIME]    # rotate clockwise
        #["ccw", DEGREES, ROTATION_EXEC_TIME]   # rotate counter-clockwise
        ]

# mission pad detected (not constant)
PAD_DETECTED = False
