#창문의 개폐 여부를 알 수 있는 reed 스위치 
reed = 19
reed1 = 6
GPIO.setup(reed, GPIO.IN)
GPIO.setup(reed1, GPIO.IN)
def get_pos():
   pos=""
   if GPIO.input(reed)==0 or GPIO.input(reed1)==0: #둘 중 하나라도 자석에 닿아 있으면 창문이 열린 상태
       pos="open"
   if GPIO.input(reed)==1 and GPIO.input(reed1)==1: # 둘 다 자석에 떨어져 있으면 창문이 닫힌 상태
       pos="close"
   return pos
