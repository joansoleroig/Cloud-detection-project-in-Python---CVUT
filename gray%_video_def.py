import cv2
import numpy as np
from settings import settings
cap, gray, diff, boundaries, gray_low, gray_high = settings('video_sky.mp4', 210, 210, 210, 45)
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cv_img=[] 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True: 
    # Display the resulting frame
    #cv2.imshow('Frame',frame)
    cv_img.append(frame)
    clouds_detected =cv2.inRange(frame,gray_low,gray_high)
    frame[clouds_detected>0]=(255,255,255)
    cv2.imshow('Spotted clouds',frame)
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()

##IMAGE BY IMAGE GRAY %
n=0
gray_list=[]
for (lower, upper) in boundaries:
    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    for image in cv_img:
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        ratio_gray1 = cv2.countNonZero(mask)/(image.size/3)
        n=n+1
        rounded=np.round(ratio_gray1*100, 2)
        sentence = 'gray pixel percentage of image '
        print(sentence + str(n) +" is: "+ str(rounded))
        gray_list.append(rounded)
        if n<5:
            message='Stop the machine\n'
            f = open("observations.txt", "a")
            f.write(str(n)+';'+str(rounded)+';'"Not enough data"+';'+message)
            f.close()
        else:
            sublist=gray_list[n-5:n-1]
            mean_last_four=np.round(sum(sublist)/4,2)
            if rounded>17:
                message='Stop the machine\n'
                f = open("observations.txt", "a")
                f.write(str(n)+';'+str(rounded)+';'+str(mean_last_four)+';'+message)
                f.close()
            elif rounded > mean_last_four and rounded > 14:
                message='Stop the machine\n'
                f = open("observations.txt", "a")
                f.write(str(n)+';'+str(rounded)+';'+str(mean_last_four)+';'+message)
                f.close()
            else:
                message='Keep the machine ON\n'
                f = open("observations.txt", "a")
                f.write(str(n)+';'+str(rounded)+';'+str(mean_last_four)+';'+message)
                f.close()            


 
