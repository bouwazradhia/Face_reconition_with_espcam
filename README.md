# Face_reconition_with_espcam

Requirements:

Libraries Used:

> 1-face_recognition:

Description: A face recognition library built with dlib and designed to work with images and videos.
#### Installation: pip install face_recognition
Documentation: face_recognition GitHub

> 2-cv2 (OpenCV):

Description: Open Source Computer Vision Library for image and video processing.
#### Installation: pip install opencv-python
Documentation: OpenCV Documentation

> 3-imutils:

Description: A series of convenience functions to make basic image processing functions such as resizing, rotation, and displaying images easier.
#### Installation: pip install imutils
Documentation: imutils GitHub

> 4-os:

Description: Python's standard library module for interacting with the operating system, used for file and directory operations.
#### Documentation: os Module Documentation

> 5-WebcamVideoStream (imutils.video):

Description: 
Part of the imutils library, providing a threaded video stream class for efficient webcam access.
#### Installation: pip install imutils
Documentation: imutils GitHub
These libraries are essential for various tasks in the script, including face recognition, video stream handling, image processing, and operating system interactions. Ensure they are installed using the provided installation commands before running the script. Links to documentation are included for further reference.

> Setup:

Set the path for your reference image: your_image_path = "****/****.jpg"
Configure the directory containing images: image_directory = "****"
Run the Script:

Connect the ESP32 camera and update the url variable with the camera stream URL.
Execute the script: python your_script_name.py
Press 'q' to exit the program.
Important Notes:

Ensure a stable network connection for ESPcam streaming.
The script performs real-time face recognition on the video stream.
Detected faces will be framed, and corresponding names will be displayed.
Customization:

Adjust the your_image_path variable to the path of your reference image.
Configure the image_directory variable for the directory containing comparison images.
Modify the url variable to match the ESPcam stream URL.
Exiting:

Press the 'q' key to terminate the program.
Troubleshooting:

Ensure all required libraries are installed.
Check the network connection for ESPcam streaming.
Verify the correct paths and URLs in the script.
Feel free to customize image paths, directories, and any other parameters as needed for your specific use case. If you encounter issues, refer to the troubleshooting section and make necessary adjustments.

