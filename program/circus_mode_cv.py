import time
import threading
import cv2

import config
import drone
import command
import cmd_dispatcher as cd
import obj_recoginition as obj_rec
import position



"""
def start():
     # temp var
    current_score = None
    previous_score = None

    # start the drone and stream
    drone_inst = drone.Drone
    recvThread = threading.Thread(target=drone_inst.recv)
    recvThread.start()

    pos = position.Position(start_position=[0,0,80,0])

    drone_inst.send("command")
    time.sleep(1)
    drone_inst.send("streamon")
    time.sleep(1)

    cmd_to = command.Command("takeoff", None)
    cmd_cw = command.Command("cw", 10)
    cmd_ccw = command.Command("ccw", 10)

    drone_inst.send("takeoff")
    time.sleep(8)
    # rotate by 10° and score image
    for i in range(36):
        # score pic
        while True:
            if config.CURRENT_IMG_SET:
                print("there is a img set")
                img = config.CURRENT_IMG
                cv2.imshow("current image", img)
                current_score = obj_rec(img)

            else:
                time.sleep(1)


        print(f"rotation - degree {(i+1) * 10}")
        # get pic
        # score pic
        # roteate

"""
import datetime

def start():

    print("######## start circus mode")
    # start the drone and stream
    drone_inst = drone.Drone()
    recvThread = threading.Thread(target=drone_inst.recv)
    recvThread.start()

    # pos = position.Position(start_position=[0, 0, 80, 0])

    drone_inst.send("command")
    time.sleep(1)
    drone_inst.send("streamon")
    time.sleep(1)

    time.sleep(10)
    """
    cmd_to = command.Command("takeoff", None)
    cmd_cw = command.Command("cw", 10)
    cmd_ccw = command.Command("ccw", 10)
    """
    drone_inst.send("takeoff")
    time.sleep(8)
    # rotate by 10° and score image
    img = config.CURRENT_IMG
    print(img)
    # write
    cv2.imwrite('{}_{}.{}'.format(
        "/home/monika/",
        datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'),
        'jpg'), img)

    for i in range(10):
        drone_inst.send("ccw 5")
        time.sleep(2)
        img = config.CURRENT_IMG
        print(img)
        # write
        cv2.imwrite('{}_{}.{}'.format(
            "/home/monika/",
            datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'),
            'jpg'), img)

    drone_inst.send("land")



    """
    while not config.CURRENT_IMG_SET:
        print("no image yet")
        if config.CURRENT_IMG_SET:
            print("there is a img set")
            # start the drone and stream
            drone_inst = drone.Drone
            recvThread = threading.Thread(target=drone_inst.recv)
            recvThread.start()

           # pos = position.Position(start_position=[0, 0, 80, 0])

            drone_inst.send("command")
            time.sleep(1)
            drone_inst.send("streamon")
            time.sleep(1)

            cmd_to = command.Command("takeoff", None)
            cmd_cw = command.Command("cw", 10)
            cmd_ccw = command.Command("ccw", 10)

            drone_inst.send("takeoff")
            time.sleep(8)
            # rotate by 10° and score image
            img = config.CURRENT_IMG
            print(img)
            # write
            cv2.imwrite('{}_{}.{}'.format(
                "/home/monika/",
                datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'),
                'jpg'), img)

            #for i in range(6):

            #cv2.imshow("current image", img)
            break
"""

#start()