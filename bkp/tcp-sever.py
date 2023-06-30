














''''
import socket
import threading
import time
# 建立一个服务端
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 以下设置解决ctrl+c退出后端口号占用问题
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',8001)) #绑定要监听的地址（内网ip）和端口
server.listen(5) #开始监听 表示可以使用五个链接排队
print('listen')
conn, addr = server.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
print(conn, addr)
num = 0
def run(n):
    data = conn.recv(1024)  #接收数据
    if  data:
        print('recive:', data.decode())  # 打印接收到的数据

while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
    print('连接成功')
    t1 = threading.Thread(target=run, args=("thread 1",))
    t1.start()
    time.sleep(2)
    conn.sendall(b"success")
    print('send:',num)  # 打印接收到的数据
    num=num+1
    # conn.close()

'''