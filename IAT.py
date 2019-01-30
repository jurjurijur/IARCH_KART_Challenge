import RPi.GPIO as GPIO
import time
  
#WIELEN
def rijRecht():
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins_left[pin], halfstep_seq[halfstep][pin])
      GPIO.output(control_pins_rechts[pin], halfstep_seq[halfstep][pin])
    time.sleep(0.001)
    #print("rectdoor")

def draaiLinks():
 for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins_left[pin], halfstep_seq_rev[halfstep][pin])
      GPIO.output(control_pins_rechts[pin], halfstep_seq[halfstep][pin])
    time.sleep(0.001)
    #print("Linksaf")

def draaiRechts():
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins_left[pin], halfstep_seq[halfstep][pin])
      GPIO.output(control_pins_rechts[pin], halfstep_seq_rev[halfstep][pin])
    time.sleep(0.001)
    #print("Recht")

#ACTIES
def bochtLinks():
  while GPIO.input(8) == 0:
    draaiLinks()
  #for tel in range(10):
   # draaiLinks()
  return
def bochtRechts():
  while GPIO.input(12) == 0:
    draaiRechts()
 # for tel in range(10):
  #  draaiRechts()
  return
def splitsing():
  print("split")
  keuze = "r"
  if keuze == "r":
    for step in range(150):
      rijRecht()
    for step in range(800):
      #print("bezigheid")
      draaiRechts()
  if keuze == "s":
      rijRecht()
  return
# ZWART === 0!!!!!!
# WIT ==== 1!!!!

#Benoemen van de inputs
def printZicht():
    zicht = ["l = "+ str(GPIO.input(8)),"m= " + str(GPIO.input(10)),"r =" + str(GPIO.input(12))]
    return zicht

def detectWeg():
  #print("aan het detecteren")
#Rechdoor
  if GPIO.input(8) == 1 and GPIO.input(12) == 1:
    rijRecht()
  elif GPIO.input(8) == 0 and GPIO.input(10) == 0 and GPIO.input(12) ==  0:
    print("splitsing")
    splitsing()
  elif GPIO.input(8) == 1 and GPIO.input(10) == 1 and GPIO.input(12) ==  1:
    rijRecht()
  #LINKS
  elif GPIO.input(8) == 0 and GPIO.input(10) == 1 and GPIO.input(12) == 1:
    bochtLinks()
  elif GPIO.input(8) == 0 and GPIO.input(10) == 0 and GPIO.input(12) == 1:
    bochtLinks()
  elif GPIO.input(8) == 0 and GPIO.input(10) == 0 and GPIO.input(12) == 1:
    bocht()
  #Rechts
  elif GPIO.input(12) == 0 and GPIO.input(8) == 1 and GPIO.input(10) == 1:
    bochtRechts()
  elif GPIO.input(12) == 0 and GPIO.input(8) == 0 and GPIO.input(10) == 1:
    bochtRechts()
  elif GPIO.input(8) == 1 and GPIO.input(10) == 0 and GPIO.input(12) == 0:
    bochtRechts()
  print(printZicht())
# MAIN 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(12, GPIO.IN)
bezig = True
control_pins_left = [11, 7, 5, 3]
control_pins_rechts = [13, 15, 19, 21]

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


halfstep_seq_rev = [
  [1,0,0,1],
  [0,0,0,1],
  [0,0,1,1],
  [0,0,1,0],
  [0,1,1,0],
  [0,1,0,0],
  [1,1,0,0],
  [1,0,0,0],
]

for pin in control_pins_left:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

for pin in control_pins_rechts:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

while bezig == True:
  try:
     detectWeg()
  except KeyboardInterrupt:
    GPIO.cleanup()

