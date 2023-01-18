
import array

import paho.mqtt.client as mqtt

array_size = 10

# Create an array to store the ADC data
adc_data = array.array("H", [0] * array_size)


array_pratap = []
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("outTopicPratap")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    for i in range(array_size):
        print(msg.topic + " " + str(msg.payload))
        print(str(msg.payload, "utf-8"))
        array_pratap = msg.payload
        print(type(array_pratap))
        array_pratap = int(array_pratap)
        # Read the ADC data and store it in the array
        adc_data[i] = array_pratap
    print (adc_data)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect("broker.hivemq.com", 1883, 8000)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

# Create an analog input object
# Define the size of the array
