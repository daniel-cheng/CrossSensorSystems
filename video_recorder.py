import subprocess
import time
import os
import Video_Client

def record(seconds):
	filename = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())

	# Command for video and audio together
	#cmd = "avconv -f video4linux2 -r 24 -i /dev/video0 -f alsa -i plughw:CARD=C525,DEV=0 -ar 22050 -ab 64k -strict experimental -acodec aac -vcodec mpeg4 -t 00:00:" + str(seconds) + " /var/www/html/videos/" + filename + "i-va.mp4"
	# Command for video only
	cmd = "avconv -f video4linux2 -r 24 -i /dev/video0 -vcodec mpeg4 -t 00:00:" + str(seconds) + " /var/www/html/videos/" + filename + "-v.mp4"
	subprocess.call(cmd, shell=True)
	Video_Client.File_Send()	

	
if __name__== "__main__":
	while (True):
		record(30)
		path = "/var/www/html/videos"
		now = time.time()
		for f in os.listdir(path):
			f = os.path.join(path, f)
			if os.stat(f).st_mtime < now - 1800:
				if os.path.isfile(f):
					os.remove(os.path.join(path, f))

