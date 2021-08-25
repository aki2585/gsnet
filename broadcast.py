from socket import *
import datetime
import time
from art import *
HOST = ''
PORT = 392585
ADDRESS = "255.255.255.255" # 自分に送信

art1 = art("random")

s = socket(AF_INET, SOCK_DGRAM)
# ブロードキャストする場合は、ADDRESSを
# ブロードキャスト用に設定して、以下のコメントを外す
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    dt6= datetime.datetime.now()
    strdt6 = dt6.strftime('%Y-%m-%d %H:%M:%S.%f')
    art1 = art("random")
    msg = strdt6 + "\n" + art1 + "\n"
    print(art1)
    # 送信
    s.sendto(msg.encode(), (ADDRESS, PORT))
    time.sleep(1)
s.close()
