# import the necessary packages
# python3 pi_face_recognition.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle --output dataset/Unknown
#python3 pi_face_recognition.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle --output dataset/Unknown --out dataset/Blocked
from imutils.video import VideoStream
from imutils.video import FPS
import paho.mqtt.client as mqtt
import face_recognition
import sys

import argparse
import imutils
import pickle
import time
import cv2
import os


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
	help = "path to where the face cascade resides")
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory")
ap.add_argument("-ou", "--out", required=True,
				help="path to output directory")
args = vars(ap.parse_args())

total = 0
t = 0

if not os.path.exists(args["output"]):
        os.makedirs(args["output"])
if not os.path.exists(args["out"]):
		os.makedirs(args["out"])
# load the known faces and embeddings along with OpenCV's Haar
# cascade for face detection
print("[INFO] loading encodings + face detector...")
data = pickle.loads(open(args["encodings"], "rb").read())
detector = cv2.CascadeClassifier(args["cascade"])

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# start the FPS counter
fps = FPS().start()

# loop over frames from the video file stream
################################################




while True:

	# def on_connect1(stop_ai, userdata, flags, rc):
	# 	print("Connected with result code " + str(rc))
	# 	stop_ai.subscribe("zezo", 1)
	#
	#
	# def pub1():
	# 	stop_ai.publish('ziko', "ziko", 1)
	#
	#
	# def on_message1( stop_ai, userdata, msg):
	# 	# msg.topic = msg.topic.decode("utf-8")
	# 	msg.payload = msg.payload.decode("utf-8")
	#
	# 	if "zezo" in msg.topic:
	# 		print("hello")
	# 		os.abort()
	#
	#
	#
	#
	#
	# stop_ai = mqtt.Client()
	#
	# stop_ai.username_pw_set('mbncsfqo', 'nHJRekh2bOFx')
	# stop_ai.on_connect = on_connect1
	# stop_ai.on_message = on_message1
	#
	# stop_ai.connect('hairdresser.cloudmqtt.com', 18914, 60)
	# stop_ai.loop_start()
	# time.sleep(0.30)
	# stop_ai.loop_stop()


























	# grab the frame from the threaded video stream and resize it
	# to 500px (to speedup processing)
	frame = vs.read()
	frame = imutils.resize(frame, width=500)

	# convert the input frame from (1) BGR to grayscale (for face
	# detection) and (2) from BGR to RGB (for face recognition)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# detect faces in the grayscale frame
	rects = detector.detectMultiScale(gray, scaleFactor=1.1,
		minNeighbors=5, minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE)

	# OpenCV returns bounding box coordinates in (x, y, w, h) order
	# but we need them in (top, right, bottom, left) order, so we
	# need to do a bit of reordering
	boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

	# compute the facial embeddings for each face bounding box
	encodings = face_recognition.face_encodings(rgb, boxes)
	names = []

	# loop over the facial embeddings
	for encoding in encodings:
		# attempt to match each face in the input image to our known
		# encodings
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		name = "Unknown"

		# check to see if we have found a match
		if True in matches:
			# find the indexes of all matched faces then initialize a
			# dictionary to count the total number of times each face
			# was matched
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			# loop over the matched indexes and maintain a count for
			# each recognized face face
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			# determine the recognized face with the largest number
			# of votes (note: in the event of an unlikely tie Python
			# will select first entry in the dictionary)
			name = max(counts, key=counts.get)

		# update the list of names
		names.append(name)

	if any("Block" in words for words in names) and (len(names) is not 0):
		ts = os.path.sep.join([args["out"], "{}.png".format(str(total / 10).zfill(5))])
		cv2.imwrite(ts, rgb)
		t +=1
		if t % 40 == 0:

			def on_connect( hady, userdata, flags, rc):
				print("Connected with result code " + str(rc))
				hady.subscribe('blocked', 1)


			def pub():
				hady.publish('blocked', 'toz', 1)


			hady = mqtt.Client()
			hady.username_pw_set('mbncsfqo', 'nHJRekh2bOFx')
			hady.on_connect = on_connect
			hady.connect('hairdresser.cloudmqtt.com', 18914, 60)
			pub()

			print("there is blocked person")
	else:
		t = 0
#################################################################################################### s 30 frame
	if (all(word == 'Unknown' for word in names)) and (len(names) is not 0):
		ts = os.path.sep.join([args["output"], "{}.png".format(str(total / 10).zfill(5))])
		cv2.imwrite(ts, rgb)

		total += 1
		if total % 40 == 0:



			def on_connect(self, client, userdata, flags, rc):
				print("Connected with result code " + str(rc))
				client.subscribe('blocked', 1)


			def pub():
				client.publish('blocked', 'toz',  1)



			client = mqtt.Client()
			client.username_pw_set('mbncsfqo', 'nHJRekh2bOFx')
			client.on_connect = on_connect
			client.connect('hairdresser.cloudmqtt.com', 18914, 60)
			pub()
			print("hello")
			#client.loop_forever()





	else:
		total =0
################################################################################################
	# loop over the recognized faces
	for ((top, right, bottom, left), name) in zip(boxes, names):
 		# draw the predicted face name on the image
 		cv2.rectangle(frame, (left, top), (right, bottom),
 			(0, 255, 0), 2)
 		y = top - 15 if top - 15 > 15 else top + 15
 		cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
 			0.75, (0, 255, 0), 2)

	# display the image to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	# if key == ord("q"):
	# 	break
















	# update the FPS counter
	fps.update()












# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
