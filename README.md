# Project-2-CVUT
This is the repository for Project 2.


The code reads the last 5 images, the 5th being the newest one, the current one.
We read them and calculate the percentage of grey and white inside the picture of the 5 photos.

Then we set 2 conditions:
The machine will stop if the last picture has a % of over 50% of gray and white.
And the machine will also stop whenever it ahs a % of over 30% & the 5th picture is over the mean of the past 4 images.

The code returns whether the macihne should stop or keep running.
