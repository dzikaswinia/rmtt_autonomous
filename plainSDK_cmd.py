# DCPC - drone control per command (SDK)

import socket
import threading

cmd_ip = '192.168.10.1'
cmd_port = 8889
host_ip = '0.0.0.0'
response_port = 9000

print("RMTT program")

class Drone:
    def __init__(self):
        self._running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((host_ip, response_port))

    def terminate(self):
        self._running = False
        self.sock.close()

    def recv(self):
        while self._running:
            try:
                msg, _ = self.sock.recvfrom(1024)
                utf8 = 'utf-8'
                print(f'response {msg.decode(encoding=utf8)}')
            except Exception as err:
                print(err)

    def send(self, msg):
        msg = msg.encode(encoding='utf-8')
        self.sock.sendto(msg, (cmd_ip, cmd_port))
        print(f'message: {msg}')


drone = Drone()
recvThread = threading.Thread(target=drone.recv)
recvThread.start()

while True:
    try:
        msg = input()
        print('Input: ' + msg)
        drone.send(msg)

        if msg == 'bye':
            drone.terminate()
            recvThread.join()
            print('\nGood bye\n')
            break

    except KeyboardInterrupt:
        drone.terminate()
        recvThread.join()
        break

    