from simple import MQTTClient 
from machine import Pin 
import dht 
import network 
import time 
import ujson
import network  
SERVER = "192.168.1.101" 
CLIENT_ID = "0TO17SZU94547OGY" 
TOPIC = "home/zyf/dht11" 

def run():     
  while True:         
    gpin_dht = Pin(4)
    d = dht.DHT11(gpin_dht)
    d.measure()
    temperture = d.temperature() 
    print(str(temperture))
    print('Temperature: ' + str(temperture) + ' Celsius')
    #up_temp1 ="{\"sensorDatas\":[{\"sensorsId\":200314505,\"value\":"+str(temperature)+"}]}"
    up_temp1="{ \"temp\":"+str(temperture) +" }"
    c.publish(TOPIC,up_temp1,retain=True)           
    print(up_temp1)            
    time.sleep(3)  
server=SERVER 
c = MQTTClient(CLIENT_ID,server) 
c.connect() 
print("Before MQTT publish") 
run() 
print("MQTT published...............")
    


