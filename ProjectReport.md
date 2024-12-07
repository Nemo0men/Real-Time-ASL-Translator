## Team Name: 
AI Brawlers

## Team Members:
Bryan Tang, 
Nemo Kim,
Davis Wang

## Project Introduction:
SignScribe: An AI powered real time sign language translator platform
Description: Communication barriers exist for individuals who are deaf or hard of hearing, as sign language is not universally understood. This project aims to bridge that gap by developing a portable, AI-driven device capable of recognizing sign language gestures in real-time using an Arduino TinyML kit. By translating hand gestures into text or speech, this system can facilitate smoother interactions
Objective: Develop a Real-Time Gesture Recognition Model: Train and deploy a deep learning model on the Arduino TinyML kit that accurately recognizes sign language gestures in real time.

## Technology Stack: 
Ardunio TinyML Kit, Ardunio Nano 33 BLE; OV7675 Camera; Micro USB cable

## Software:
Ardunio IDE; Python Compiler (VS code), Edge Impulse, Google Collab

## Step 1: Image Capture (Set up Arduino IDE and GUI + collecting images for dataset) 
1. Download the Ardunio IDE and install following Ardunio packages by:
   - Open the Arduino IDE. Go to Tools > Board > Boards Manager.... Search for "nano 33" in the boards manager pane. Install the Arduino Mbed OS Nano Boards board package.
   - Open the Arduino IDE. Go to Tools > Manage Libraries > .... Search for "OV7675". Install the Arduino_OV767X library.
2. Install packages for python: pip install Pillow pyserial
3. Connect Ardunio to computer through micro USB cable, and change the board to the correct port at the top of the Ardunio IDE. Should be listed as: Arduino Nano 33 BLE.
4. Go to Files > Examples > Arduino_OV767X > Camera Capture... Open up the camera set up program and upload the code to the board.
5. Download and Open up the GUI code in the repo listed as (CamGUI.py) > run the program with the board attached and change the port to the same port listed on the Arduino IDE.
6. Pick out specific ASL handsigns and take about 50-60 pictures of each one at different angles (make sure to label them with what each one is). Take another 50-60 images of a background
7. Once all the images are saved and move them to a single folder and zip that folder to a compressed ZIP folder.

## Step 2: Image Translations (Take images and upload them to Edge Impulse)
1. Open up Google Collab Notebook: https://colab.research.google.com/github/edgeimpulse/workshop-arduino-tinyml-roshambo/blob/main/02-data-augmentation/ei-image-augmentation.ipynb
2. Upload ZIP file with images into google collab notebook > right click > Upload > ZIP Folder
3. Make an Edge Impulse Account and navigate to create first project
- Navigate to Dashboard > Keys> copy the API key
4. Copy the API key into section 3 in the google collab code where it's listed.
5. Run each block of the google collab code...This should augment images and upload them to Edge Impulse for training and testing
- The images can be seen uploaded in Edge Impulse by navigating to > Data Aquisatition > Should have a roughly 75/25 split of images for Train/Test split.





