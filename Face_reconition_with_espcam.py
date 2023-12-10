import face_recognition
import cv2
from imutils.video import WebcamVideoStream
import imutils
import os

# Load your image
your_image_path = "dhia/dhia.jpg"
your_image = face_recognition.load_image_file(your_image_path)
your_face_encoding = face_recognition.face_encodings(your_image)[0]

# Path to the directory containing images
image_directory = "dhia"

# Get a list of all image files in the directory
image_files = [f for f in os.listdir(image_directory) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

# List to store face encodings of all images
known_face_encodings = []
known_face_names = []

# Load face encodings for all images in the directory
for image_file in image_files:
    image_path = os.path.join(image_directory, image_file)
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(face_encoding)
    known_face_names.append(os.path.splitext(image_file)[0])

# Open the video stream
url = 'http://***.***.***.***:81/stream'
cap = WebcamVideoStream(url).start()

while True:
    frame = cap.read()

    # Resize the frame to improve processing speed
    frame = imutils.resize(frame, width=600)

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known face
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # If a match is found, use the name of the first matching known face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw rectangle around the face and display the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close all windows
cap.stop()
cv2.destroyAllWindows()
