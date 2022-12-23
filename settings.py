import cv2
import numpy as np
def settings(video_name, RGB1, RGB2, RGB3, tolerances):
    cap = cv2.VideoCapture(video_name)
    gray = [RGB1, RGB2, RGB3]  # RGB
    diff = tolerances
    boundaries = [([gray[2]-diff, gray[1]-diff, gray[0]-diff],
               [gray[2]+diff, gray[1]+diff, gray[0]+diff])]
    gray_low=np.array([gray[2]-diff, gray[1]-diff, gray[0]-diff])
    gray_high=np.array([gray[2]+diff, gray[1]+diff, gray[0]+diff])
    return cap, gray, diff, boundaries,gray_low,gray_high
