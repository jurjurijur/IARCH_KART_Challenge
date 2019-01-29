class Wiel(object):
#initializer
    def __init__(control_pins):
        self.control_pins = control_pins
        self.start(self.control_pins)

    def start():
        for pin in self.control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
            self.halfstep_seq = [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]
            ]
            
    def drive(sleep):
        for i in range(512):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.control_pins[pin], self.halfstep_seq[halfstep][pin])
            time.sleep(sleep)


    def stop():
        GPIO.cleanup()