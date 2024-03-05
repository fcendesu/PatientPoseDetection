# Patient Movement Detection
## Overview
The Head Movement Detection project is a simple application built with Flask and OpenCV to detect and record head movements in real-time. The primary aim is to monitor whether a patient moves their head for more than 3 seconds continuously. The application utilizes computer vision techniques to identify facial features and analyze head movements.
Features
Real-time head movement detection using OpenCV.
Records date and time of head movements lasting more than 2 seconds.
Web interface for easy interaction.

## Features
Real-time Head Movement Detection:

The application captures video from the user's camera and uses a Haar Cascade classifier to detect frontal faces in each frame.
Head Movement Logging:

If head movement is detected for more than 3 seconds, the application logs the event along with a timestamp in the 'head_movements.log' file.

## Dependencies
Flask
OpenCV
(Other dependencies listed in requirements.txt)
