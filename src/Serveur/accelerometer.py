# @author Mehdi BOUAFIA using what Louise have done

import numpy as np
import os
import cv2
import platform
from datetime import datetime
import time

frames_per_second = 24.0
res = '720p'

# Standard Video Dimensions Sizes
STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

# Set resolution for the video capture
# Function adapted from https://kirr.co/0l6qmh


def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)


# grab resolution dimensions and set video capture to it.
def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    # change the current caputre device
    # to the resulting resolution
    change_res(cap, width, height)
    return width, height


def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


def Video_Accelerometer(user):
    my_os = platform.system()
    now = datetime.now()  # current date and time
    if my_os == "Windows":
        filename = "Accelerometer\\" + user + '_' + \
            now.strftime("%m_%d_%Y_%H%M") + ".avi"
    else:
        filename = "Accelerometer/" + user + '_' + \
            now.strftime("%m_%d_%Y_%H%M") + ".avi"

    cap2 = cv2.VideoCapture(0)
    out2 = cv2.VideoWriter(filename, get_video_type(
        filename), 25, get_dims(cap2, res))
    start = time.time()
    while True:
        
        ret2, frame2 = cap2.read()
        out2.write(frame2)
        cv2.imshow('frame2', frame2)
        # your code
        stop = time.time()
       
        if stop-start > 60 :
            break

    cap2.release()
    out2.release()
    cv2.destroyAllWindows()
