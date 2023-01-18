import paho.mqtt.client as mqtt

# Initialize the moving average filter with a window size of 10
window_size = 10
values = []
raw = []
avg_array = []
avg = 0

# MQTT callback function for when a message is received
def on_message(client, userdata, message):
    global values
    global avg
    # Add the new value to the list of values
    values.append(float(message.payload))
    raw.append(float(message.payload))
    avg_array.append (avg)
    # If the list of values is larger than the window size, remove the oldest value
    if len(values) > window_size:
        values.pop(0)
        raw.pop(0)
        avg_array.pop(0)


    # Calculate the moving average
    avg = sum(values) / len(values)
    # print("Moving average:",values)
    print("RAW DATA ARRAY:", raw)
    print("Moving average:", avg_array)
    print("Raw Data:  ", values[-1])
    print("Avg Data:  ", avg_array[-1])


# Initialize the MQTT client and set the callback function
client = mqtt.Client()
client.on_message = on_message

# Connect to the MQTT broker
client.connect("broker.hivemq.com")

# Subscribe to a topic
client.subscribe("outTopicPratap")

# Start the MQTT client loop to receive messages
client.loop_forever()
