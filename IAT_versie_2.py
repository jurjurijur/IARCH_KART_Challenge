import RPi.GPIO as GPIO
import time
from Tkinter import *  


#WIELEN
def rijRecht():
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins_left[pin], halfstep_seq[halfstep][pin])
      GPIO.output(control_pins_rechts[pin], halfstep_seq[halfstep][pin])
    time.sleep(0.001)
    #print("rechtdoor")
def scherpRechts():
 for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins_left[pin], halfstep_seq[halfstep][pin])
    time.sleep(0.001)
    print("srechts")
def scherpLinks():
 for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins_rechts[pin], halfstep_seq[halfstep][pin])
    time.sleep(0.001)
    print("slinks")
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
def scherpeBochtRechts():
  while GPIO.input(12) == 0:
    scherpRechts()
 # for tel in range(10):
  #  draaiRechts()
  return
def scherpeBochtLinks():
  while GPIO.input(8) == 0:
    scherpLinks()
 # for tel in range(10):
  #  draaiRechts()
  return
def dubbelCheck():
  print("dubblecheck")
  for tel in range(4):
    rijRecht()
  if GPIO.input(8) == 0 and GPIO.input(12) ==  0:
    print("splitsing")
    splitsing(maxSplitsing)
    return True
  else:
    return False
  
def splitsing(maxSplitsing):
  global aantalSplitsingGehad
  print("split")
  global inputRichting
  if maxSplitsing > aantalSplitsingGehad:
    if inputRichting == 3:
      for step in range(150):
        rijRecht()
      for step in range(200):
        #print("bezigheid")
        draaiRechts()
    if inputRichting == 2:
      for step in range(150):
        rijRecht()
    if inputRichting == 1:
      for step in range(150):
        rijRecht()
      for step in range(250):
        #print("bezigheid")
        draaiLinks()
    aantalSplitsingGehad += 1
    print(maxSplitsing, aantalSplitsingGehad)
    return
  else:
    einde()
    return
# ZWART === 0!!!!!!
# WIT ==== 1!!!!

#Benoemen van de inputs
def printZicht():
    zicht = ["l = "+ str(GPIO.input(8)),"m= " + str(GPIO.input(10)),"r =" + str(GPIO.input(12))]
    return zicht

def detectWeg():
  print("check")
  #print("aan het detecteren")
#Rechdoor and GPIO.input(10) == 0 
  if GPIO.input(8) == 0 and GPIO.input(12) ==  0:
    print("splitsing")
    splitsing(maxSplitsing)
  elif GPIO.input(8) == 1 and GPIO.input(12) == 1:
    rijRecht()
  elif GPIO.input(8) == 1 and GPIO.input(10) == 1 and GPIO.input(12) ==  1:
    rijRecht()
#LINKS
  elif GPIO.input(8) == 0 and GPIO.input(10) == 0 and GPIO.input(12) == 1:
    if dubbelCheck() == True:
      print("dubbelcheck 1")
    elif dubbelCheck() == False:
      print("bocht links")
      bochtLinks()
  elif GPIO.input(8) == 0 and GPIO.input(10) == 1 and GPIO.input(12) == 1:
    bochtLinks()
#Rechts
  elif GPIO.input(12) == 0 and GPIO.input(8) == 1 and GPIO.input(10) == 1:
    bochtRechts()
  elif GPIO.input(8) == 1 and GPIO.input(10) == 0 and GPIO.input(12) == 0:
    if dubbelCheck() == True:
      print("dubbelcheck 1")
    elif dubbelCheck() == False:
      print("bocht rechts")
      bochtRechts()
  print(printZicht())
#Cmmunicatie
def sel():
    global inputRichting
    print(str(var.get()))
    keuze = var.get()
    beweging = "nergens heen"
    if keuze == 1:
      inputRichting = 1
      beweging = "linksaf"
    elif keuze == 2:
      inputRichting = 2
      beweging = "rechtdoor"
    elif keuze == 3:
      inputRichting = 3
      beweging = "rechtsaf"
    selection = "De auto gaat " + beweging
    label.config(text = selection)
    window.title("Keuzerichting kart")

def exitNu():
  window.destroy()

def exitNu2():
  einde.destroy()

def einde():
  einde = Tk()
  einde.title("Finish")
  einde.geometry("300x100+300+300")
  w = Label(einde, text = "De auto heeft de finish gehaald!")
  w.pack()
  mainloop()
 


  
# MAIN 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(12, GPIO.IN)
bezig = True
control_pins_left = [11, 7, 5, 3]
control_pins_rechts = [13, 15, 19, 21]
aantalSplitsingGehad = 0
maxSplitsing = 1
inputRichting = 0

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

window = Tk()
window.title("Keuzerichting auto")
window.geometry("300x120+300+300")
window.grid()
v = StringVar()
Label(window, textvariable=v).pack()
v.set("Kies een richting voor de auto:")
var = IntVar()
R1 = Radiobutton(window, text="Linksaf", variable=var, value=1,
                      command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(window, text="Rechtdoor", variable=var, value=2,
                      command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(window, text="Rechtsaf", variable=var, value=3,
                      command=sel)
R3.pack( anchor = W)

button = Button(window, text = "Bevestig", command = exitNu)
button.pack()
label = Label(window)
label.pack()
window.mainloop()

while bezig == True:
  try:
   detectWeg()
  except KeyboardInterrupt:
    GPIO.cleanup()

