import paho.mqtt.client as mqtt

class my_mqtt():
    def __init__(self):
        pass




    def on_connect(self,client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe('momo',0 )

    def on_message(self,client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
    def pub ():
        client.publish(topic_name, message, 1)

    def into (self):

        client = mqtt.Client()
        client.username_pw_set('mbncsfqo', 'nHJRekh2bOFx')
        client.on_connect = on_connect
        pub()
        client.connect('hairdresser.cloudmqtt.com', 18914, 60)
        client.loop_forever()

        client.on_message = on_message









