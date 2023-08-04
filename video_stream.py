import cv2
import robomaster
from robomaster import robot

robomaster.config.LOCAL_IP_STR = "0.0.0.0"

drone = robot.Drone()
drone.initialize()
camera = drone.camera
camera.start_video_stream(display=False)
camera.set_fps("high")
camera.set_resolution("high")
camera.set_bitrate(6)
for i in range(0, 302):
    img = camera.read_cv2_image()
    cv2.imshow("Drone", img)
    cv2.waitKey(1)
cv2.destroyAllWindows()
camera.stop_video_stream()
drone.close()
