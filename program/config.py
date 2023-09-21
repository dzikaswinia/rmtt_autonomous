
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
MOVE = [15, 20, 30, 40, 60, 80, 100]        # cm
MOVE_UP_DOWN = [60, 80, 120]    # cm
DEGREES = [90, 180]        # degrees  TODO extend with 270° but will position tracking still work?
CMDS = [["takeoff", None, TAKEOFF_EXEC_TIME],
        ["land", None, 0],
        #["up", MOVE_UP_DOWN, MOVE_EXEC_TIME],
        #["down", MOVE_UP_DOWN, MOVE_EXEC_TIME],
        ["forward", MOVE, MOVE_EXEC_TIME],
        ["back", MOVE, MOVE_EXEC_TIME],
        ["left", MOVE, MOVE_EXEC_TIME],
        ["right", MOVE, MOVE_EXEC_TIME],
        ["cw", DEGREES, ROTATION_EXEC_TIME]    # rotate clockwise
        #["ccw", DEGREES, ROTATION_EXEC_TIME]   # rotate counter-clockwise
        ]

CMDS_obstacles = [["forward", MOVE, MOVE_EXEC_TIME],
        ["cw", DEGREES, ROTATION_EXEC_TIME],    # rotate clockwise
        ["ccw", DEGREES, ROTATION_EXEC_TIME]   # rotate counter-clockwise
        ]

# mission pad detected (not constant)
PAD_DETECTED = False
PAD = 0
CURRENT_X = None    # position of the drone relative to the mission pad
CURRENT_Y = None
TOLERANCE = 5

# TODO loe?
MOVE_CMD_RESP = ""
GET_CMD_REPS = ""

# ---- circus mode ----------
THRESHOLD = 5   # for x and y coordinate of the mission pads


# 2pads approach
DIST_BETWEEN_PADS = 35          # distance between pad #1 and #2
TOLERANCE_FORWARD = [0, 0, 0]        # added to the distance when searching for the pad #1
TOLERANCE_BACKWARD = [0, 0, 0]
#TOLERANCE_FORWARD = [10, 15, 20]        # added to the distance when searching for the pad #1
#TOLERANCE_BACKWARD = [0, 10, 15]

# CV approach
CURRENT_IMG = None
CURRENT_IMG_SET = False

CEN_COR_VAL = 0         # correction value for centering function (drone tends to fly further than it is ask to)

REVERSE_CMD_NAMES = {
        'forward': 'back',
        'back': 'forward',
        'right': 'left',
        'left': 'right' }
