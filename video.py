from picamera import PiCamera
import time
import datetime

camera = PiCamera()

camera.framerate = 30
camera.resolution = (640, 480)
camera.color_effects = (128, 128)
camera.start_preview()
tstamp = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
camera.start_recording('KarlPi_' + tstamp + '.h264')
time.sleep(20)
camera.stop_recording()
camera.stop_preview()
