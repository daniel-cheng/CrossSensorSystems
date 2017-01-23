# CrossSensorSystems
Architectural implementation of low-bandwidth, high quality audio-visual stream processing for the purpose of high-level data analysis.

This python script will run a face detection video analysis server, accessible at localhost:8080/index.html.

Setup:
Raspberry Pi 3 running Raspbian.
Install OpenCV and Python 2.
Run this script by executing "python2.7  opencv_mjpeg_server.py"

You may view the install_opencv.sh script to view additional dependecies, including the python packages numpy, pillow, and imutils.
It is advised to use a virtual environment to manage your python installation and the screen utility to run the server indefinitely.

For full installation instructions of OpenCV for python, please see http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/.
Credit to milq for the original install_opencv.sh script, see https://github.com/milq/scripts-ubuntu-debian/blob/master/install-opencv.sh.
