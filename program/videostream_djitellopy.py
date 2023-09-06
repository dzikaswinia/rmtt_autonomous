import time, cv2
from threading import Thread
from djitellopy import Tello


print("setup")
tello = Tello()
tello.connect()

print("start")
keepRecording = True
tello.streamon()
tello.set_video_direction(Tello.CAMERA_FORWARD)
tello.set_video_fps(Tello.FPS_30)
frame_read = tello.get_frame_read()

def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    # 创建一个VideoWrite对象，存储画面至./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

recorder = Thread(target=videoRecorder)
recorder.start()

tello.takeoff()
tello.move_up(100)
tello.rotate_counter_clockwise(360)
tello.land()

keepRecording = False
recorder.join()


"""
for i in range(0, 25):
    print("img")
    img = tello.get_frame_read().frame
    print(f'we have img')
    #img = cv2.resize(img, (648, 488))
    cv2.imshow("image", img)
"""


print("end")
#keepRecording = True
#tello.streamon()
#frame_read = tello.get_frame_read()

"""
tello.connect()
tello.takeoff()
tello.land()
"""