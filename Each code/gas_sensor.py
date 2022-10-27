#ADC를 하기 위해 spi통신을 이용
spi = spidev.SpiDev()       # spi 객체를 만듬
spi.open(0,0)               # spi 버스 번호와 CS(Chip Select) 번호를 이용하여 사용할 버스를 open하여야 함.
spi.max_speed_hz = 1000000  #최대 속도는 1MHz로 설정

def analogRead(ch):  # 아날로그신호 읽어드림
   buf = [(1<<2)|(1<<1)|(ch&4)>>2, (ch&3)<<6 ,0]      # 2번째있는 비트를 1로 or 첫번쨰있는비트1 or (ch&4)>>2, buf[1] = (ch&3)<<6 ,  buf[2] = 0
   buf= spi.xfer(buf)                                 # spi.xfer([1,2,4,5,0]) 이렇게 그냥 값만을 전달하는 함수여서 원하는 주소에 값을보냄
   adcValue = ((buf[1]&0xF)<<8)|buf[2]            # buf[1]과 0xF는 8번 왼쪽으로 시프트 or buf[2]
   return adcValue
