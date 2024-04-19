# 15-puzzle-and-mechatronics
A mechatronics projects that physically solves 15-puzzle using a 3D printer and A* algorithm


Physical setup as shown: 
(add picture)


The code in this repo works in the following steps: 
1. Establishing SSH connection to Raspberry Pi
2. Instructing RPi to use the camera to take a photo and send back to PC
3. Process the image with OpenCV using binarization and morphological operations (and rotation and cropping)
4. Crop the processed image to 16 sections, then feed each to easyOCR to extract the initial state of the puzzle
5. Feed the initial state to A* algorithm and check whether it is solvable
6. If solvable, generate the path and movements required
7. Convert the movements to gcode
8. Connect to 3D printer controller via WiFi using Selenium, then send the gcode and start "printing"


A document will be added to detail the required modifications if you want to use this setup (once I finish that...)
