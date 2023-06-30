# udp-server.py
from socket import *

host = '127.0.0.1'
port = 8000

# 创建server socket
server_socket = socket(AF_INET,SOCK_DGRAM)

# 绑定socket监听地址
server_addr = (host,port)
server_socket.bind(server_addr)

print('UDP Server Start...')

# 处理连接请求
while(True):
    # 接收客户端的数据
    data, addr = server_socket.recvfrom(1024)
    print("Receive from %s:%s" % addr % data)
    if data == b"quit":
        server_socket.sendto(b"Good bye!\n", addr)
        continue
    server_socket.sendto(b"Hello,udp client!\n", addr)