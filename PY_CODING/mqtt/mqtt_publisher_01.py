
#https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker ="broker.hivemq.com"

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker, 1883, 8000)

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)