import socket
import config


class Drone:
    def __init__(self):
        self._running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((config.HOST_IP, config.RESP_PORT))

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
        self.sock.sendto(msg, (config.CMD_IP, config.CMD_PORT))
        print(f'message: {msg}')


# ------------------- TESTS ---------------------