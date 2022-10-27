import os
import fcntl
I2C_SLAVE = 0x703 #주소
PM2008 = 0x28     #주소
fd = os.open('/dev/i2c-1', os.O_RDWR) #I2C 버스 open
if fd < 0 :#fd가 <0이라면
   print("i2c열기 실패\n")#fail i2c open 출력 
io = fcntl.ioctl(fd, I2C_SLAVE,PM2008)
if io < 0 :#io가 <0이라면
   print("버스 권한접근실패, SLAVE로 통하시오.\n")
def dust_get():
    global PM01
    global PM25
    global PM10
    dust = os.read(fd,32)
    PM01 = 256*int(dust[7])+int(dust[8])
    PM25 = 256*int(dust[9])+int(dust[10])
    PM10 = 256*int(dust[11])+int(dust[12])
