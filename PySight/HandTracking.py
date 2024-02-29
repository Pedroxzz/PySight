import cv2
import mediapipe as mp
import time

video_capture = cv2.VideoCapture(0)

while True:
    success, img = video_capture.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)