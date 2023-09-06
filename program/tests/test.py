import djitellopy
from djitellopy import Tello
import cv2



tello = Tello()
#tello.connect()
print(f'camera forward: {Tello.CAMERA_FORWARD}, downward: {Tello.CAMERA_DOWNWARD}')

"""
tello.streamon()
print(f"bitrate: {Tello.BITRATE_5MBPS}")
tello.set_video_bitrate(Tello.BITRATE_1MBPS)
frame = tello.get_frame_read()
print("kk")
for i in range(0, 100):
    #print(f"frame: {frame.frame}")
    #print(f'Shape: {frame.frame.shape}')
    #print("------------")
    #cv2.imshow("jj", frame.frame)
    img = frame.frame
    cv2.imshow("jj", img)
tello.set_video_fps(Tello.FPS_30)
frame = tello.get_frame_read()
print("kk")
for i in range(0, 5):
    print("start")
    img = frame.frame
    cv2.imshow("jj", img)
    print("end")
"""
