import threading
import socket
import time
import cv2

import config


class Stream:
    def __init__(self):
        self._running = True
        self.video = cv2.VideoCapture("udp://@0.0.0.0:11111")

    def terminate(self):
        self._running = False
        self.video.release()
        cv2.destroyAllWindows()

    def recv(self):
        """ Handler for Tello states message """
        while self._running:
            try:
                ret, frame = self.video.read()
                #print(f"ret: {ret}, {type(ret)}")
                #print(f"frame: {frame}, {type(frame)}")
                if ret:
                    # Resize frame
                    height, width, _ = frame.shape
                    new_h = int(height / 2)
                    new_w = int(width / 2)

                    # Resize for improved performance
                    new_frame = cv2.resize(frame, (new_w, new_h))

                    config.CURRENT_IMG = new_frame
                    config.CURRENT_IMG_SET = True
                    """
                    if config.CURRENT_IMG_SET:
                        print("image is set !")
                        """
                    # Display the resulting frame
                    # cv2.imshow('Tello', new_frame)
                # Wait for display image frame
                #cv2.waitKey(1) & 0xFF == ord('q'):
                #cv2.waitKey(1)
            except Exception as err:
                print(err)


def run_stream():
    print("stream function started")
    time.sleep(3)
    t = Stream()
    recvThread = threading.Thread(target=t.recv)
    recvThread.start()
    print("start thread")
    while True:
        try:
            # Get input from CLI
            msg = input()

            # Check for "end"
            if msg == "bye":
                t.terminate()
                recvThread.join()
                print("\nGood Bye\n")
                break
        except KeyboardInterrupt:
            t.terminate()
            recvThread.join()
            break





# --------------- test -----------------------
#run_stream()