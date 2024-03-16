import socket


class Command():
    def __init__(self, TELLO_IP, TELLO_PORT):
        # UDP通信ソケットの作成(アドレスファミリ：AF_INET（IPv4）、ソケットタイプ：SOCK_DGRAM（UDP）)
        self.TELLO_IP = TELLO_IP
        self.TELLO_PORT = TELLO_PORT
        self.TELLO_ADDRESS = (TELLO_IP, TELLO_PORT)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 自ホストで使用するIPアドレスとポート番号を設定
        self.sock.bind(('', self.TELLO_PORT))

    # 離陸
    def takeoff(self):
        print("-----")
        try:
            sent = self.sock.sendto('takeoff'.encode(encoding="utf-8"), self.TELLO_ADDRESS)
        except:
            pass
    # 着陸
    def land(self):
        try:
            sent = self.sock.sendto('land'.encode(encoding="utf-8"), self.TELLO_ADDRESS)
        except:
            pass
    # 上昇(20cm)
    def up(self, distance):
        try:
            sent = self.sock.sendto(('up %d' % distance).encode(encoding="utf-8"), self.TELLO_ADDRESS)
        except:
            pass
    # 下降(20cm)
    def down(self, distance):
        try:
            
            sent = self.sock.sendto(('down %d' % distance).encode(encoding="utf-8"), self.TELLO_ADDRESS)
        except:
            pass
    # 前に進む(20cm)
    def forward(self, distance):
        try:
            sent = self.sock.sendto(('forward %d' % distance).encode(encoding="utf-8"), self.TELLO_ADDRESS)
        except:
            pass
    # 後に進む(20cm)
    def back(self, distance):
        try:
            sent = self.sock.sendto(('back %d' % distance).encode(encoding="utf-8"), self.TELLO_ADDRESS)
        except:
            pass
    # 右に進む(20cm)
    def right(self, distance):
        try:
            sent = self.sock.sendto(('right %d' % distance).encode(encoding="utf-8"), self.TELLO_ADDRESS)
        except:
            pass
    # 左に進む(20cm)
    def left(self, distance):
        try:
            sent = self.sock.sendto(('left %d' % distance).encode(encoding="utf-8"), self.TELLO_ADDRESS)
        except:
            pass
    # # 右回りに回転(90 deg)
    # def cw(self):
    #     try:
    #         sent = self.sock.sendto('cw 90'.encode(encoding="utf-8"), self.TELLO_ADDRESS)
    #     except:
    #         pass
    # # 左回りに回転(90 deg)
    # def ccw(self):
    #     try:
    #         sent = self.sock.sendto('ccw 90'.encode(encoding="utf-8"), self.TELLO_ADDRESS)
    #     except:
    #         pass
    # # 高速モード(速度40cm/sec)
    # def speed40(self):
    #     try:
    #         sent = self.sock.sendto('speed 40'.encode(encoding="utf-8"), self.TELLO_ADDRESS)
    #     except:
    #         pass
    # # 低速モード(速度20cm/sec)
    # def speed20(self):
    #     try:
    #         sent = self.sock.sendto('speed 20'.encode(encoding="utf-8"), self.TELLO_ADDRESS)
    #     except:
    #         pass
    # 緊急停止
    def emergency(self):
        try:
            sent = self.sock.sendto('emergency'.encode(encoding="utf-8"), self.TELLO_ADDRESS)
        except:
            pass
