from simple import MQTTClient
from machine import Pin
import network
import time
import ujson
import network

#LED_PIN = PWM(Pin(2))
led=Pin(2, Pin.OUT) 

SERVER = "192.168.1.101"
CLIENT_ID = "umqtt_zyfabba23"
TOPIC = b"home/zyf/dht11"
c = None
def sub_cb(topic,msg):
  global state
  print((topic,msg))
#  print(type(msg))
  infor = msg.decode()
  print('infor is:' + infor)
 # print(type(infor))  
  inforJson = ujson.loads(infor)
  obj=ujson.loads(msg.decode())
  #obj = ujson.loads(msg.decode())
 # sensorsId1 = obj['ID']
#  print(sensorsId1)
  valuel = obj['temp']
#  print(str(valuel))
#  print("温度传感器："+str(sensorsId1)+"值为："+str(valuel)+"摄氏度")
  print("温度传感器："+str(valuel))

  if valuel > 28:
    led.value(1) 
  else :
    led.value(0)

server = SERVER
c = MQTTClient(CLIENT_ID,server)
c.set_callback(sub_cb)
c.connect()
c.subscribe(TOPIC)
print("Connected to %s,subscribed to %s topic" % (server,TOPIC))
while True:
   c.check_msg()
   time.sleep(1)
   
