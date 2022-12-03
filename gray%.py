import numpy as np
import cv2


## READ ALL IMAGES
img1 = cv2.imread('dark_sky.jpeg', 1)
img2 = cv2.imread('cloud 2.jpg', 1)
img3 = cv2.imread('sky 3.jpg', 1)
img4 = cv2.imread('sky 4.jpeg', 1)
img5 = cv2.imread('sky 5.jpg', 1)

##DEFINE GRAY/WHITE COLOR RANGES
gray = [210, 210, 210]  # RGB
diff = 40
boundaries = [([gray[2]-diff, gray[1]-diff, gray[0]-diff],
               [gray[2]+diff, gray[1]+diff, gray[0]+diff])]

##IMAGE BY IMAGE GRAY %
# IMAGE 1
for (lower, upper) in boundaries:
    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    mask = cv2.inRange(img1, lower, upper)
    output = cv2.bitwise_and(img1, img1, mask=mask)

    ratio_gray1 = cv2.countNonZero(mask)/(img1.size/3)
    print('gray pixel percentage of image 1:', np.round(ratio_gray1*100, 2))

    cv2.imshow("images", np.hstack([img1, output]))
    cv2.waitKey(0)



# IMAGE 2

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    mask = cv2.inRange(img2, lower, upper)
    output = cv2.bitwise_and(img2, img2, mask=mask)

    ratio_gray2 = cv2.countNonZero(mask)/(img2.size/3)
    print('gray pixel percentage of image 2:', np.round(ratio_gray2*100, 2))

    cv2.imshow("images", np.hstack([img2, output]))
    cv2.waitKey(0)


# IMAGE 3

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    mask = cv2.inRange(img3, lower, upper)
    output = cv2.bitwise_and(img3, img3, mask=mask)

    ratio_gray3 = cv2.countNonZero(mask)/(img3.size/3)
    print('gray pixel percentage of image 3:', np.round(ratio_gray3*100, 2))

    cv2.imshow("images", np.hstack([img3, output]))
    cv2.waitKey(0)

# IMAGE 4

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    mask = cv2.inRange(img4, lower, upper)
    output = cv2.bitwise_and(img4, img4, mask=mask)

    ratio_gray4 = cv2.countNonZero(mask)/(img4.size/3)
    print('gray pixel percentage of image 4:', np.round(ratio_gray4*100, 2))

    cv2.imshow("images", np.hstack([img4, output]))
    cv2.waitKey(0)

# IMAGE 5

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    mask = cv2.inRange(img5, lower, upper)
    output = cv2.bitwise_and(img5, img5, mask=mask)

    ratio_gray5 = cv2.countNonZero(mask)/(img5.size/3)
    print('gray pixel percentage of image 5:', np.round(ratio_gray5*100, 2))

    cv2.imshow("images", np.hstack([img5, output]))
    cv2.waitKey(0)

#This program will tell us to shut down the machine whenever one of this 2 conditions is met:
#Whenever the clouds in picture 5 cover over 50% of the image
    
mean_of_last_4_pictures = 100*(ratio_gray1 + ratio_gray2 + ratio_gray3 + ratio_gray4)/4
print(mean_of_last_4_pictures)

if ratio_gray5 > 50:
    print('Stop the machine')


#Whenever the last picture is over the mean of the last 5 and is over 30%
elif ratio_gray5 > mean_of_last_4_pictures and ratio_gray5 > 30:
    print('Stop the machine')
else:
    print('The machine is fine')
