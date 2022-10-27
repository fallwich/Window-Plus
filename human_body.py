people = 16
led = 19
GPIO.setup(led, GPIO.OUT)
GPIO.setup(people, GPIO.IN)
try:
    while True:
        GPIO.output(led, GPIO.LOW)       
        elif GPIO.input(people) ==1:
            GPIO.output(led, GPIO.HIGH)  #인체 감지 시 led on 후에 침입자 사진 찍는 곳에 활용
        time.sleep(2)
except KeyboardInterrupt:
    pass
