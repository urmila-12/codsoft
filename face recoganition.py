
import cv2 as cv
import face_recognition
import matplotlib.pyplot as plt


known_image = face_recognition.load_image_file("urmila.jpeg")
known_faces = face_recognition.face_encodings(face_image = known_image,
											num_jitters=50,
											model='large')[0]

cam = cv.VideoCapture(0)
if not cam.isOpened():
	print("Camera not working")
	exit()
	
while True:
	
	ret, frame = cam.read()
	
	if not ret:
		print("Can't receive the frame")
		break

	face_locations = face_recognition.face_locations(frame)

	for face_location in face_locations:
		top, right, bottom, left = face_location
		frame = cv.rectangle(frame, (right,top), (left,bottom), color = (0,0, 255), thickness=2)
	try:
		Live_face_encoding = face_recognition.face_encodings(face_image = frame,
															num_jitters=23,
															model='large')[0]

		results = face_recognition.compare_faces([known_faces], Live_face_encoding)

		if results:
			img = cv.cvtColor(frame, cv2.COLOR_BGR2RGB)
			img = cv.putText(img, 'urmila', (30, 55), cv2.FONT_HERSHEY_SIMPLEX, 1,
					(255,0,0), 2, cv2.LINE_AA)
			print('urmila Enter....')
			plt.imshow(img)
			plt.show()
			break
	except:
		img = cv.putText(frame, 'Not urmila', (30, 55), cv2.FONT_HERSHEY_SIMPLEX, 1,
				(255,0,0), 2, cv2.LINE_AA)
		cv.imshow('frame', img)
		if cv.waitKey(1) == ord('q'):
			break
	

cam.release()
cv.destroyAllWindows()
