KarlVonPi is a set of python scripts and set up instructions designed for the programmatic recording of honey bee behavior. The immediate context of the work is the recording of waggle dance behavior for subsequent decoding, but these scripts could be adapted for any application in which programmatic video recording is needed.

Materials:
RaspberryPi 3 B+ computer (with power source, peripherals, OS, etc.)
ArduCam NOIR

This approach uses the ArduCam NOIR RaspberryPi camera. The appeal of this camera is its ability to switch on or off an infrared filter, thus enabling good quality recording in a range of light conditions. It comes with twin IR LEDs that switch on in low light conditions to provide IR illumination, enabling video to be recorded in total darkness as long as the subject is within a few feet of the camera. Note that the IR LEDs will reflect off the glass of an observation hive, creating two small circles of glare that obscure the bees. This is probably not a critical problem since most dance behavior will occur outside the glare. A solution would be to use indirect IR illumination, but that would require addition equipment.

Start by downloading the software needed to operate the IR filter switch. The following instructions are found on https://github.com/ArduCAM/RPI_Motorized_IRCut_Control

-------------------

You have to disable the automatic management of camera led in /boot/config.txt.

$ sudo echo "disable_camera_led=1" >> /boot/config.txt 
$ sudo reboot
If permission denied you can do

$ sudo nano /boot/config.txt
add "disable_camera_led=1" at the file end. Then save the file and reboot .

$ sudo reboot

Installation
$ wget https://raw.githubusercontent.com/arducam/RPI_Motorized_IRCut_Control/master/CameraLED.py 
$ chmod 755 CameraLED.py

-------------------

For indoor observation hives, lighting conditions are almost always poor, so the instruction below assume that the IR filter should be set to "off".

# Turn off IR filter
$ python CameraLED.py off

Now run video record script.


