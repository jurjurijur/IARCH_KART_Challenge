import RPi.GPIO as GPIO
import time
import Wiel


wielLinks = Wiel.Wiel([11, 7, 5, 3])
wielRecht = Wiel.Wiel([13, 15, 19, 21])

wielLinks.start()
wielRecht.start()

try:
  wielLinks.drive(0.1)
  wielRecht.drive(0.1)
except KeyboardInterrupt:
   wielLinks.stop(0.1)
   wielRecht.stop(0.1)
