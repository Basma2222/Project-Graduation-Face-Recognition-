import paho.mqtt.client as mqtt
import os
def on_connect1(stop_ai, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    stop_ai.subscribe("ziko", 1)


def pub1():
    stop_ai.publish('ziko', "ziko", 1)





def on_message1(stop_ai, userdata, msg):
        # msg.topic = msg.topic.decode("utf-8")
        msg.payload = msg.payload.decode("utf-8")
        if "hello" in msg.payload:
            print("hello")
stop_ai = mqtt.Client()
stop_ai.username_pw_set('mbncsfqo', 'nHJRekh2bOFx')
stop_ai.on_connect = on_connect1

stop_ai.connect('hairdresser.cloudmqtt.com', 18914, 60)
stop_ai.on_message = on_message1



stop_ai.loop_forever()