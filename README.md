# Project-2-CVUT
This is the repository for Project 2.


The aim of the project is to detect the clouds in the sky and make a decision to stop the machine when there are too many clouds.
The code reads a video, frame by frame and it culatesthe percentage of grey and white inside the frame. This is done through RGB color detection.

Then we set 2 conditions:
The machine will stop if the last picture has a % of over 50% of gray and white.
And the machine will also stop whenever it has % of over 30% of the 5th frame is over the mean of the last 4 frames.

The code returns whether the macihne should stop or keep running.
The code also retruns the video with the % at each frame of the video as well as the message at every moment.
The code finally writes a .txt file prepared to be opened as csv in excel to be further analysed and it writes the information of each frame.
We can later conduct the analysis of the excel file and see how many times the machines has been stopped/running.
