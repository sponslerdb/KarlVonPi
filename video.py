from picamera import PiCamera
import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import logging
import subprocess

# I don't really understand this section, but it has to do with formatting the
# logging of the scheduler loop
log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG
fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)

# Camera settings; run these outside the job loop
camera = PiCamera()
camera.framerate = 30 # 30 fps
camera.resolution = (640, 480) # lower than default to minimize file size
camera.color_effects = (128, 128) # b&w

# Prep sched command
sched = BlockingScheduler()

# run script every 15 minutes between 10am and 2pm, 7 days/wk
@sched.scheduled_job('cron', day_of_week='mon-sun', 
                     hour='10-14', minute='0-59/15', 
                     timezone='America/New_York')
def scheduled_job():
    camera.start_preview()
    tstamp = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") # get timestamp
    camera.start_recording('Karl_' + tstamp + '.h264') # write to file
    time.sleep(120) # record 2 minute video
    camera.stop_recording()
    camera.stop_preview()

# Need to figure out how to subprocess the output to my server

sched.start()



