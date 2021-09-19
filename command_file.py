import os
import paho.mqtt.client as mqtt
from pathlib import Path
import shutil
import sys



def on_connect(hady, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    hady.subscribe('add', 1)
    hady.subscribe('delete', 1)
    hady.subscribe('enableai', 1)




def pub():
    hady.publish('ziko', "ziko", 1)
    #hady.publish('delete', "not found", 1)


   # hady.publish('name', 'ziko', 1)
def on_message(hady, userdata, msg):
    #msg.topic = msg.topic.decode("utf-8")
    msg.payload = msg.payload.decode("utf-8")
    if "add" in msg.topic:
        os.system("service motion stop")
        os.system("python3 build_face_dataset.py --cascade haarcascade_frontalface_default.xml --output dataset/"+str(msg.payload))
        os.system("python3 encode_faces.py --dataset dataset --encodings encodings.pickle --detection-method hog")
        os.system("python3 pi_face_recognition.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle --output dataset/Unknown --out dataset/Blocked")
        os.system("pkill -f fepy")
    if "delete" in msg.topic:
        #os.system("service motion stop")



        dirpath = Path('dataset',msg.payload )
        if dirpath.exists() and dirpath.is_dir():
            shutil.rmtree(dirpath)
            os.system("python3 encode_faces.py --dataset dataset --encodings encodings.pickle --detection-method hog")
        else:

            hady.publish('notfound', "not found", 1)
            print('not found')
    if "enableai" in msg.topic:
        os.system("python3 pi_face_recognition.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle --output dataset/Unknown --out dataset/Blocked")













hady = mqtt.Client()
hady.username_pw_set('mbncsfqo', 'nHJRekh2bOFx')
hady.on_connect = on_connect

#os.system("python3 build_face_dataset.py --cascade haarcascade_frontalface_default.xml --output dataset/ziko")
hady.on_message = on_message
#.connect('hairdresser.cloudmqtt.com', 18914, 60)
hady.connect_async('hairdresser.cloudmqtt.com',18914, 60)

hady.loop_forever()


#python3 build_face_dataset.py --cascade haarcascade_frontalface_default.xml --output dataset/YOUR_NAME

# if 'abas' in mqtt.payload:
#os.system("python3 build_face_dataset.py --cascade haarcascade_frontalface_default.xml --output dataset/"+hady.subscribe('name', 1))


