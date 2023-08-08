import threading
import socket
import time


def convert_to_matrix_row_format(item):
    # stripping from unnecessary symbols
    item = item[1:]  # remove byte symbol
    item = item[:-6]
    l = item.split(';')  # converts each parameter into separate list element
    result = ''
    for i in range(len(l)):
        val = l[i].split(':')
        result += val[1]
        if i < len(l) - 1:
            result += ':'
    return result


file_path = "/home/monika/Dokumente/robotik/drone_state/state_230808-1.txt" # bobik
#file_path = "/home/monika/nauka/Robotik/drone_state/state_230808-1.txt" # mikus
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 8890))
file = open(file_path, "a")

#for x in range(100):
while True:
    try:
        print('trying to get sensor state')
        data, server = sock.recvfrom(1024)
        print(data.decode())
        file.write(convert_to_matrix_row_format(str(data)) + "\n")
    except Exception as err:
        print(err)
        sock.close()
        file.close()
        break

"""
class Tello:
    def __init__(self):
        self._running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((host_ip, response_port))

    def terminate(self):
        self._running = False
        self.sock.close()

    def recv(self):
        print("recv")
        while self._running:
            print("tello is running")
            try:
                msg, _ = self.sock.recvfrom(1024)
                print("msg received")
                state = msg.decode()
                print(f'state: {state}')
            except Exception as err:
                print(err)


host_ip = "0.0.0.0"
response_port = 8890

print("Tello Sensor State")

t = Tello()
recvThread = threading.Thread(target=t.recv())
recvThread.start()
print("thread started")
while True:
    try:
        print("we are in try")
        msg2 = input("Input: ")
        if msg2 == "bye":
            t.terminate()
            recvThread.join()
            print("\nDo widzenia!")
            break

    except KeyboardInterrupt:
        t.terminate()
        recvThread.join()
        break
"""
