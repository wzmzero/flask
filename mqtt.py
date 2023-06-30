import paho.mqtt.client as mqtt
import random
import time
from datetime import datetime
# MQTT代理信息
broker_address = "122.51.127.33"
broker_port = 1883

# 连接回调函数
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")

# 发布消息
def publish_message(client, topic, message):
    client.publish(topic, message)
    print("Published message:", message, "to topic:", topic)

# 创建MQTT客户端
client = mqtt.Client()

# 设置连接回调函数
client.on_connect = on_connect

# 连接到MQTT代理
client.connect(broker_address, broker_port, 60)

# 循环发布随机数到主题
while True:
    random_number = random.randint(1, 100)
    topic = "/topic"
    message = str(random_number)+'---'+str(datetime.now())

    publish_message(client, topic, message)

    time.sleep(1)  # 每隔1秒发布一次随机数
