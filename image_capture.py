import numpy as np
import cv2
import RPi.GPIO as GPIO
#from gpiozero import LED, Button
#from time import sleep
from flirpy.camera.boson import Boson
#from tifffile import imsave

channel = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
count = 0

#callback to be executed at the rising pulse
def my_callback(channel):
    if GPIO.input(channel) == 1:
        cv2.imwrite("/home/pi/Desktop/Boson_thermal_jpg/Boson%d.jpg" % count, img_re.astype(np.uint8))
        imsave("/home/pi/Desktop/Boson_thermal_tiff/Boson_tiff%d.tiff" % count, img)
        global count
        count = count + 1
        #print('rising pulse')

# rising pulse detection at gpio
GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback, bouncetime=1)

#main loop
with Boson() as camera:
    while(True):
        img = camera.grab().astype(np.float32)
        img_re = 255*(img - img.min())/(img.max()-img.min()) #image re-scaling
        #cv2.imshow('Boson', img_re.astype(np.uint8)) 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()
