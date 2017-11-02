import paho.mqtt.client as mqtt 
import random
# Define Variables
MQTT_BROKER = "104.236.18.145"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "testNew"


# Define on_connect event Handler
def on_connect(mosq, obj, rc):
	print("Connected to MQTT Broker")

# Define on_publish event Handler
def on_publish(client, userdata, mid):
	print(MQTT_MSG)

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect


# Connect with MQTT Broker
mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 
while True:
	MQTT_MSG = "hello"
	mqttc.publish(MQTT_TOPIC,MQTT_MSG)

# Disconnect from MQTT_Broker
mqttc.disconnect()
