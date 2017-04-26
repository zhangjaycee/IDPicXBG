# IDPicXBG

### a program intending for changing a ID card photo's background

* based on opencv2 for python

* By default, the background color being changed to is white

* the output file will guarenteed larger than 40K. (by doing Expansion Transformation if the source photo is to0 small...)

### how to use it:

./main.py [PATH_TO_PHOTO]
the processed photo will be saved to dst.jpg in current DIR.

### how to install opencvlib for python:

for macOS:

~~~bash
brew install gtk+
brew install opencv
cp /usr/local/Cellar/opencv/2.4.13.2/lib/python2.7/site-packages/*  /usr/local/lib/python2.7/site-packages
~~~

for ubuntu:

~~~bash
apt install python-opencv
~~~


