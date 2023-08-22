
# cube limitations (in cm)
MAX_Y = 100
MAX_X = 100
MAX_Z = 200

# websocket for SDK cmd
CMD_IP = '192.168.10.1'
CMD_PORT = 8889
HOST_IP = '0.0.0.0'
RESP_PORT = 9000

# cmd
TAKEOFF_EXEC_TIME = 8
MOVE_EXEC_TIME = 3
ROTATION_EXEC_TIME = 2
CMDS = [#["takeoff", None],
        #["land", None],
        ["up", [20], MOVE_EXEC_TIME],
        ["down", [20], MOVE_EXEC_TIME],
        ["forward", [20, 40, 60], MOVE_EXEC_TIME],
        ["back", [20, 40, 60], MOVE_EXEC_TIME],
        ["left", [20, 40, 60], MOVE_EXEC_TIME],
        ["right", [20, 40, 60], MOVE_EXEC_TIME],
        ["cw", [90, 180], ROTATION_EXEC_TIME],    # rotate clockwise
        ["ccw", [90, 180], ROTATION_EXEC_TIME]]   # rotate counter-clockwise