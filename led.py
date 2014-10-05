import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(21, gpio.OUT)

gpio.output(17, 1)
time.sleep(2)
gpio.output(18, 1)
time.sleep(2)
gpio.output(21, 1)
time.sleep(2)

gpio.cleanup()
