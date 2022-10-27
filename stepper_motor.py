a = 27 # stepper motor
b = 17 # stepper motor
c = 22 # stepper motor
d = 18 # stepper motor

def setStepper(in1, in2, in3, in4): #setup stepper #스텝 출력 설정
    GPIO.output(a, in1)
    GPIO.output(b, in2)
    GPIO.output(c, in3)
    GPIO.output(d, in4)
    time.sleep(0.005)

def setup(): # 입출력 설정
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(a, GPIO.OUT) # stepper motor
    GPIO.setup(b, GPIO.OUT) # stepper motor
    GPIO.setup(c, GPIO.OUT) # stepper motor
    GPIO.setup(d, GPIO.OUT) # stepper motor
    
def close_window(pos): #창문이 열려있을 때만 닫을 수 있다. 1060펄스를 주어 총 1908도 회전
    if pos=="open":
        for i in range(258): # stepper motor 1060 pulse 1908 degree
            setStepper(1, 0, 0, 0)
            setStepper(0, 1, 0, 0)
            setStepper(0, 0, 1, 0)
            setStepper(0, 0, 0, 1)
            time.sleep(0.006)
            
def open_window(pos): #창문이 닫혀있을 때만 열 수 있다. 
    if pos=="close":
        for i in range(258): # stepper motor 1060 pulse 1908 degree
            setStepper(0, 0, 0, 1)
            setStepper(0, 0, 1, 0)
            setStepper(0, 1, 0, 0)
            setStepper(1, 0, 0, 0)
            time.sleep(0.006)
