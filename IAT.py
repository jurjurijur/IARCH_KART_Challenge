import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
control_pins_left = [11, 7, 5, 3]
control_pins_right = [13, 15, 19, 21]
for pin in control_pins-Left:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]
for i in range(512):
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins_left[pin], halfstep_seq[halfstep][pin])
    time.sleep(0.001)
GPIO.cleanup()