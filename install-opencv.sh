sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y dist-upgrade
sudo apt-get -y autoremove

# INSTALL THE DEPENDENCIES

# Build tools:
sudo apt-get install -y build-essential cmake pkg-config

# GUI (if you want to use GTK instead of Qt, replace 'qt5-default' with 'libgtkglext1-dev' and remove '-DWITH_QT=ON' option in CMake):
sudo apt-get install -y libgtk2.0-dev libgl1-mesa-dri

# Media I/O:
sudo apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev

# Video I/O:
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev

# Parallelism and linear algebra libraries:
sudo apt-get install -y libatlas-base-dev gfortran

# Python:
sudo apt-get install -y python2.7-dev python3-dev
wget https://bootstrap.pypa.io/get-pip.py

# Install pip and pyaudio
sudo python get-pip.py
sudo rm -rf ~/.cache/pip get-pip.py
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-devk python-pyaudio

#Create virtualenv for Python 2
pip install virtualenv virtualenvwrapper
echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.profile
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
source ~/.profile
mkvirtualenv cv -p python2
workon cv
pip install numpy pillow imutils matplotlib scipy sklearn hmmlearn simplejson eyed3 pydub 

# INSTALL THE LIBRARY (YOU CAN CHANGE '3.2.0' FOR THE LAST STABLE VERSION)
sudo apt-get install -y unzip wget
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.2.0.zip
rm -rf opencv-3.2.0
unzip opencv.zip
rm opencv.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.2.0.zip
rm -rf opencv_contrib-3.2.0
unzip opencv_contrib.zip
rm opencv_contrib.zip
cd opencv-3.2.0/modules/python/
echo -e "\n# virtualenv and virtualenvwrapper" >> common.cmake
echo "find_package(HDF5)" >> common.cmake
echo "include_directories(${HDF5_INCLUDE_DIRS})" >> common.cmake
cd ../../
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.2.0/modules \
    -D BUILD_EXAMPLES=ON ..
make -j4
sudo make install
sudo ldconfig

# Symlink OpenCV packages
cd ~/.virtualenvs/cv/lib/python2.7/site-packages/
ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so

# INSTALL FFMPEG
sudo apt-get remove libavcodec-extra-56 libavformat56 libavresample2 libavutil54
sudo wget https://github.com/ccrisan/motioneye/wiki/precompiled/ffmpeg_3.1.1-1_armhf.deb
sudo dpkg -i ffmpeg_3.1.1-1_armhf.deb

# INSTALL pyAudioAnalysis
cd ~/CrossSensorSystems
git clone https://github.com/tyiannak/pyAudioAnalysis.git 
