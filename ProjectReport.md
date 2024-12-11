### SignScribe Project Report ###

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

## Objectives, Expected Results, Known Issues, Fixes
We aimed to stablish an accurate live-capture detection system that would allow us to analyze ASL hand gestures contained within our database as they were being signed. Taking these gestures, we would track ongoing sequences of gestures and translate them into written sentences using a text generation pipeline. These texts could then be reformatted in an audio format to communicate an equivalent meaning to a corresponding user.

The expected results are to have a high accuracy in recognizing official ASL sign gestures based off the input images from snapshots of live camera feed. These images are then expected to be translated into a coherent and highly relevant sentence with full grammatical structure and syntax. 

Several known issues are directly connected to the limitations of the hardware, where the camera equipped within the Arduino Kit is only effective to a certain range. The software coupled with this camera also is limited by the camera's framerate and resolution in different environments. Edge Impulse also has some compatability issues related to the size of the dataset used for training, where a limited amount of images to form classifications with can result in significant loss through training error. 

The fixes to these issues were not entirely effective. Some adjustments were made to the software behind the camera, such as adjustments made to saturation to help the model differentiate between different hand gestures. Changes were also made to the resolution, reaching the local memory limit of our hardware and causing the compile time for each runtime to increase dramatically. The metrics for accuracy on Edge Impulse showed very promising results, but in reality our dataset did not have the depth to capture predictions for all of the gestures - only high probabilities for some gestures, rather than a few ambiguous gestures that could easily be confused with other hand signs.

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

## Step 2: Image Augmentation (Take images and upload them to Edge Impulse)
1. Open up Google Collab Notebook: https://colab.research.google.com/github/edgeimpulse/workshop-arduino-tinyml-roshambo/blob/main/02-data-augmentation/ei-image-augmentation.ipynb
2. Upload ZIP file with images into google collab notebook > right click > Upload > ZIP Folder
3. Make an Edge Impulse Account and navigate to create first project
   - Navigate to Dashboard > Keys> copy the API key
5. Copy the API key into section 3 in the google collab code where it's listed.
6. Run each block of the google collab code...This should augment images and upload them to Edge Impulse for training and testing
   - The images can be seen uploaded in Edge Impulse by navigating to > Data Aquisatition > Should have a roughly 75/25 split of images for Train/Test split.

## Step 3: Edge Impulse training
1. In Edge Impulse navigate to the impulse design tab > create impulse > change the image width and height to (30x30), and resize mode: Fit shortest axis
2. Click Add a processing block and add the Image block. Click Add a learning block and select the Classification block
3. Click on Image under Impulse design. Change the Color depth to Grayscale.
4. Click Save parameters and click Generate features on the next page. Wait while Edge Impulse generates the training features from your dataset.
   - When feature extraction is complete, you should see a 2D feature explorer showing the relative separation among the class groupings along with an estimation of the time and resources required to perform feature extraction on your target device (default: Arm Cortex-M4F).
5. Click on Classifier under Impulse design. Change the Number of training cycles (epochs) to 100. Leave everything else as default. Click Start training.
6. Navigate to the Deployment page in your project
7. In the search bar, enter Arduino and select the Arduino library option.
8. When the build process is complete, you should have an Arduino library (in .zip format) automatically downloaded to your computer.

## Step 4: Deployment and final Inferencing
1. Import the Edge Impulse library. Open the Arduino IDE. Select Sketch > Include Library > Add .ZIP Library. Select the library that you downloaded from Edge Impulse and click Open.
2. Open File > Examples > <NAME_OF_LIBRARY> > nano_ble33_sense > nano_ble33_sense_camera. Copy the #include line for your library.
3. Open 05-live-inference/nano33_camera_live_inference/nano33_camera_live_inference.ino. Paste in the library include filename for the Edge Impulse library.
4. Upload the code to your Arduino board. Compiling the Edge Impulse library will likely take a while, so be patient.
5. Once uploaded you can open up the CamGUI.py file from the image capture step > Paste in the port of your Arduino board and click Connect.
6. The terminal in the python IDE should display the inference results for the live video in frame.

## Step 5: Text Translation and Sentence Formation Using LLM
This step involves integrating a Language Model (LLM) for translating recognized ASL gestures into coherent sentences. The LLM will process gesture sequences and construct meaningful, grammatically correct sentences based on the input gesture classifications.

Prerequisites
Ensure the recognized ASL gestures (e.g., ['hello', 'my', 'name', 'is']) are returned as text predictions in sequential order from the inference pipeline.
Install required Python packages: pip install openai or any library for the LLM service you're using.

Implementation Steps
Prepare Gesture Sequence Input:

Collect gesture classification results from the Arduino's inference results (from Step 4). These should be in the form of a list of recognized words or gestures.
Integrate an LLM for Sentence Generation:

Use an LLM API like OpenAI's GPT or any other cloud-based LLM service to process the gesture sequence into a coherent sentence.
Define the Prompt:

Create a structured prompt template that provides context for the LLM to understand how to structure the gestures into a sentence.

## Code Integration Example

```python
import openai

# Configure OpenAI API key (or replace with your chosen LLM API)
openai.api_key = "your_openai_api_key"

PROMPT_TEMPLATE = """
Translate the following sequence of words into a grammatically correct sentence:

Words: {words}

Sentence:
"""

def generate_sentence(gesture_sequence):
    """
    Takes a list of recognized gestures and generates a sentence using an LLM.
    """
    # Format the prompt with the input gestures
    prompt = PROMPT_TEMPLATE.format(words=" ".join(gesture_sequence))

    # Send the prompt to the LLM API and get the response
    response = openai.Completion.create(
        engine="text-davinci-003",  # Replace with your engine
        prompt=prompt,
        max_tokens=50,
        temperature=0.7
    )
    
    # Extract the generated sentence
    generated_sentence = response.choices[0].text.strip()
    return generated_sentence

# Example usage
gesture_sequence = ['hello', 'my', 'name', 'is', 'john']
sentence = generate_sentence(gesture_sequence)
print("Generated Sentence:", sentence)









