from gpiozero import InputDevice #빗물감지 센서 작동
import time
no_rain = InputDevice(5)
led = 19
GPIO.setup(led, GPIO.OUT) #led 출력설정
try:
    while True:#빗물 감지시 led 켜진다.
        GPIO.output(led, GPIO.LOW)
        if not no_rain.is_active:
            GPIO.output(led, GPIO.HIGH)
        time.sleep(2)
except KeyboardInterrupt:
    pass
GPIO.cleanup()