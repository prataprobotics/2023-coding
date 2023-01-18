
#https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time


client = mqtt.Client("Temperature_Outside")
client.connect("broker.hivemq.com", 1883, 8000)

while True:
    randNumber = uniform(2, 10)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)