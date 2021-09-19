# pi_facerecognition
Real-time face detection/recognition project with OpenCV and Python on raspberry pi

A-build face dataset                  (build_face_dataset.py)
  -Localize faces in the image in every frame
    using OpenCV's Haar Cascades docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html
  -save image from every frame
  
B-Compute face recognition embeddings (encode_faces.py)
  -Load and convert the image to rgb
  -Localize faces in the image
  -using a deep neural network to compute a 128-d vector (i.e., a list of 128 floating point values) that will quantify each       face in the dataset and add them to knownEncodings  along with their name
  
C-Recognize faces in video streams    (pi_face_recognition.py)
  -Load the facial encodings data (knownEncodings)
  -Check for matches.
  -If matches are found we’ll use a voting system to determine whose face it most likely is.
    This method works by checking which person in the dataset has the most matches.
    
Note:
  i merge step A and B  (face_detection_encoding.py)
