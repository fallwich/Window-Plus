import os#파이썬에 내장된os모듈을 가져온다
import fcntl#fcntl 시스템 호출
import time
import RPi.GPIO as GPIO
from gpiozero import InputDevice
import spidev
import bluetooth
import Adafruit_DHT
import threading
from sys import getsizeof
from bs4 import BeautifulSoup
import requests
import json
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from datetime import date, timedelta
import datetime
from dateutil.relativedelta import relativedelta
import socket
import schedule
import picamera
sensor=Adafruit_DHT.DHT11
pin=4 #DHT11
a = 27 # stepper motor
b = 17 # stepper motor
c = 22 # stepper motor
d = 18 # stepper motor
reed = 19
reed1 = 6
people= 16
fire = 20
#reed2 =13# reed switch
no_rain = InputDevice(5) #rain drop
delay = 0.005
outdoor_button=None
indoor_button=None
gas_button=None
dust_button=None
humi_button=None
schedule_button=None
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("pwnbit.kr", 443))
ip=sock.getsockname()[0]
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) #bluetooth connect
port = 1                                                    #bluetooth connect
server_socket.bind(("",port))                               #bluetooth connect
server_socket.listen(1)                                     #bluetooth connect
client_socket,address = server_socket.accept()              #bluetooth connect
print("Accepted connection from ", address)
I2C_SLAVE = 0x703#16진수의 703 (주소)
PM2008 = 0x28#16진수의 28 (주소)
fd = os.open('/dev/i2c-1',os.O_RDWR)#I2C 버스(주변기기를 연결하기 위해 사용된다.)를 open합니다.
if fd < 0 :#fd가 <0이라면
   print("i2c열기 실패\n")#fail i2c open 출력
io = fcntl.ioctl(fd,I2C_SLAVE,PM2008)# fd
if io < 0 :#io가 <0이라면
   print("버스 권한접근실패, SLAVE로 통하시오.\n")
camera = picamera.PiCamera()
camera.resolution = (1024, 768)
def dust_get():
   global PM01
   global PM25
   global PM10
   dust = os.read(fd,32)
   PM01 = 256*int(dust[7])+int(dust[8]) #PM0.1 dust
   PM25 = 256*int(dust[9])+int(dust[10]) #PM25 dust
   PM10 = 256*int(dust[11])+int(dust[12]) #PM10 dust
   return PM01, PM25, PM10
spi = spidev.SpiDev()       # spi 객체를 만듬
spi.open(0,0)               # spi 버스 번호와 CS(Chip Select) 번호를 이용하여 사용할 버스를 open하여야 함.
spi.max_speed_hz = 1000000#최대 속도는 1MHz로 설정
token = "5450872980:AAFGO1EWbbJyFJcNcopkc3mEGnsxdf5PZiA"
id="5623439502"
id2="5350738571"
bot = telegram.Bot(token=token)
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()
#KAKAO_TOKEN="QUrl21haTLR9L1X6Jljzup72TYMl1NkTrCOlrvd_CisNHgAAAYOSSkiY"
#def sendToMeMessage(text):
 #header={"Authorization": 'Bearer ' + KAKAO_TOKEN}
 #url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
 #post = {
  #       "object_type": "text",
   #      "text": text,
    #     "link": {
     #            "web_url": "https://developers.kakao.com",
      #           "mobile_web_url": "https:/developers.kakao.com"
       #  },
        # "button_title": "바로 확인"
 #}
 #data={"template_object": json.dumps(post)}
 #return requests.post(url, headers=header, data=data)
def outdoordust_thread():
     global stationName
     global pm10Value
     global pm25Value
     global PM10_outdoor
     URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
     SERVICE_PARAM = '?serviceKey='
     SERVICE_KEY='gQj%2BcdJTZwGMhLPNhJuDPOptupzoJL7D9hJlIp6kzxp9DdqlCXxMtCPgJm%2F8kUAy0IgX0pQ5WqfgsQB26RIlVA%3D%3D'
     TYPE_PARAM = '&returnType=xml'
     ITEMS="&numOfRows=120"
     PAGE_NUM="&pageNo=1"
     SIDONAME="&sidoName=경기"
     VERSION='&ver=1.0'
     URL=URL+SERVICE_PARAM+SERVICE_KEY+TYPE_PARAM+ITEMS+PAGE_NUM+SIDONAME+VERSION
     res = requests.get(URL)
     soup = BeautifulSoup(res.text,'html.parser')
     soup.findAll('item')
     item_list = soup.findAll('item')
     stationName=[]
     pm10Value=[]
     pm25Value=[]
     for item in item_list:
         stationName.append(item.find('stationname').text)
         pm10Value.append(item.find('pm10value').text)
         pm25Value.append(item.find('pm25value').text)
     while 1:
         if decode_data in stationName:
             station_find=stationName.index(decode_data)
             print("staion:", stationName[station_find],"pm10:", pm10Value[station_find],"pm25:", pm25Value[station_find])
             PM10_outdoor=int(pm10Value[station_find])
             time.sleep(10)
         time.sleep(5)
     time.sleep(10)
def get_pos():
   pos=""
   if GPIO.input(reed)==0 or GPIO.input(reed1)==0:
       pos="open"
   if GPIO.input(reed)==1 and GPIO.input(reed1)==1:
       pos="close"
   return pos
def setStepper(in1, in2, in3, in4): #setup stepper
   GPIO.output(a, in1)
   GPIO.output(b, in2)
   GPIO.output(c, in3)
   GPIO.output(d, in4)
   time.sleep(0.005)
def setup():
   GPIO.setwarnings(False)
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(a, GPIO.OUT) # stepper motor
   GPIO.setup(b, GPIO.OUT) # stepper motor
   GPIO.setup(c, GPIO.OUT) # stepper motor
   GPIO.setup(d, GPIO.OUT) # stepper motor
   GPIO.setup(reed, GPIO.IN)
   GPIO.setup(reed1, GPIO.IN)
   GPIO.setup(people,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
   GPIO.setup(fire, GPIO.IN)
def close_window(pos):
   if pos=="open":
       for i in range(258): # stepper motor 1060 pulse 1908 degree
           setStepper(1, 0, 0, 0)
           setStepper(0, 1, 0, 0)
           setStepper(0, 0, 1, 0)
           setStepper(0, 0, 0, 1)
           time.sleep(0.001)
def open_window(pos):
   if pos=="close":
       for i in range(258): # stepper motor 1060 pulse 1908 degree
           setStepper(0, 0, 0, 1)
           setStepper(0, 0, 1, 0)
           setStepper(0, 1, 0, 0)
           setStepper(1, 0, 0, 0)
           time.sleep(0.001)
def analogRead(ch):  # 아날로그신호 읽어드림
   buf = [(1<<2)|(1<<1)|(ch&4)>>2, (ch&3)<<6 ,0]      # 2번째있는 비트를 1로 or 첫번쨰있는비트1 or (ch&4)>>2, buf[1] = (ch&3)<<6 ,  buf[2] = 0
   buf= spi.xfer(buf)                                 # spi.xfer([1,2,4,5,0]) 이렇게 그냥 값만을 전달하는 함수여서 원하는 주소에 값을보냄
   adcValue = ((buf[1]&0xF)<<8)|buf[2]            # buf[1]과 0xF는 8번 왼쪽으로 시프트 or buf[2]
   return adcValue
def dht_11_send(client_socket):
       global humi
       global temp
       humi, temp = Adafruit_DHT.read_retry(sensor, pin)
       temp_en=str(temp).encode("utf-8")
       humi_en=str(humi).encode("utf-8")
       bbb=","
       client_socket.send("777")
       client_socket.send(bbb)
       client_socket.send(temp_en)
       client_socket.send(bbb)
       client_socket.send(humi_en)
       client_socket.send(bbb)
       client_socket.send("666")
def schedule_open():
   global schedule_button
   global later2
   global present1
   pos=get_pos()
   if pos=="close":
       if no_rain.is_active:
           if PM10_outdoor<=100:
               timenow=datetime.datetime.now()
               later2=timenow+relativedelta(minutes=10)
               open_window(pos)
               schedule_button=True
               bot.send_message(chat_id=id, text="Ventilate Time")
               bot.send_message(chat_id=id2, text="Ventilate Time")
schedule.every().day.at("09:00").do(schedule_open)
schedule.every().day.at("11:00").do(schedule_open)
schedule.every().day.at("13:00").do(schedule_open)
schedule.every().day.at("15:00").do(schedule_open)
schedule.every().day.at("17:00").do(schedule_open)
schedule.every().day.at("19:00").do(schedule_open)
schedule.every().day.at("21:00").do(schedule_open)
schedule.every().day.at("01:00").do(schedule_open)
schedule.every().day.at("03:00").do(schedule_open)
schedule.every().day.at("05:00").do(schedule_open)
schedule.every().day.at("07:00").do(schedule_open)
def outdoor_mode():
           global gas_button
           global later
           global dust_button
           global humi_button
           global schedule_button
           pos=get_pos()
           dust_get()
           gasValue = analogRead(0)
           print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%" .format(temp, humi))
           if gasValue >600:
               if pos=="close":
                   timenow=datetime.datetime.now()
                   later=timenow+relativedelta(minutes=10)
                   open_window(pos)
                   gas_button=True
                   text_gas_out="Outdoor Mode - Gas Detected, Ventilates for 10 minutes "
                   bot.send_message(chat_id=id, text=text_gas_out)
                   bot.send_message(chat_id=id2, text=text_gas_out)
           present=datetime.datetime.now()
           if gas_button:
               if present>later:
                   close_window(pos)
                   gas_button=False
                   text_gas_out_later="Outdoor Mode - Gas, It's been 10 minutes, Closing the Window"
                   bot.send_message(chat_id=id, text=text_gas_out_later)
                   bot.send_message(chat_id=id2, text=text_gas_out_later)
           if PM10>80:
               if pos=="close":
                   if PM10>PM10_outdoor:
                       if no_rain.is_active:
                           timenow=datetime.datetime.now()
                           later=timenow+relativedelta(minutes=10)
                           open_window(pos)
                           dust_button=True
                           text_dust_out="Outdoor Mode - Indoor Dust exceeded 80㎍/m³, Ventilates for 10 minutes "
                           bot.send_message(chat_id=id, text=text_dust_out)
                           bot.send_message(chat_id=id2, text=text_dust_out)
           present=datetime.datetime.now()
           if dust_button:
               if present>later:
                   close_window(pos)
                   dust_button=False
                   text_dust_out_later="Outdoor Mode - Dust, It's been 10 minutes, Closing the Window"
                   bot.send_message(chat_id=id, text=text_dust_out_later)
                   bot.send_message(chat_id=id2, text=text_dust_out_later)
           if humi>75:
               if pos=="close":
                   if no_rain.is_active:
                       if PM10_outdoor<=100:
                           timenow=datetime.datetime.now()
                           later=timenow+relativedelta(minutes=10)
                           open_window(pos)
                           humi_button=True
                           text_humi_out="Outdoor Mode - Humidity exceeded 75%, Ventilates for 10 minutes"
                           bot.send_message(chat_id=id, text=text_humi_out)
                           bot.send_message(chat_id=id2, text=text_humi_out)
           present=datetime.datetime.now()
           if humi_button:
               if present>later:
                   close_window(pos)
                   humi_button=False
                   text_humi_out_later="Outdoor Mode - Humidity, It's been 10 minutes, Closing the Window"
                   bot.send_message(chat_id=id, text=text_humi_out_later)
                   bot.send_message(chat_id=id2, text=text_humi_out_later)
           if not no_rain.is_active:
               if pos == "open":
                   if gasValue<= 600:
                       close_window(pos)
                       text_rain = "Outdoor Mode - It's Raining, Shut down the Ventilation"
                       bot.send_message(chat_id=id, text=text_rain)
                       bot.send_message(chat_id=id2, text=text_rain)
                       humi_button=False
                       dust_button=False
                       gas_button=False
                       schedule_button=False
           if GPIO.input(20) == False:
               bot.send_message(chat_id=id, text="Detected Fire!\n")
               bot.send_message(chat_id=id2, text="Detected Fire!\n")
               camera.capture('fire' + '.jpg')
               bot.send_photo(chat_id=id, photo=open('/home/pi/Desktop/fire.jpg','rb'))
               bot.send_photo(chat_id=id2, photo=open('/home/pi/Desktop/fire.jpg','rb'))
               time.sleep(5)
           if GPIO.input(16) == True:
               bot.send_message(chat_id=id, text="Detected Invasion!")
               bot.send_message(chat_id=id2, text="Detected Invasion!")
               camera.capture('invasion' + '.jpg')
               bot.send_photo(chat_id=id, photo=open('/home/pi/Desktop/invasion.jpg','rb'))
               bot.send_photo(chat_id=id2, photo=open('/home/pi/Desktop/invasion.jpg','rb'))
               time.sleep(5)
           schedule.run_pending()
           present1=datetime.datetime.now()
           if schedule_button:
               if present1>later2:
                   close_window(pos)
                   schedule_button=False
                   bot.send_message(chat_id=id, text="Ventilation is done")
                   bot.send_message(chat_id=id2, text="Ventilation is done")
def indoor_mode():
       global gas_button
       global later
       global dust_button
       global humi_button
       global schedule_button
       pos=get_pos()
       dust_get()
       gasValue = analogRead(0)
       print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%" .format(temp, humi))
       if gasValue >400:
           if pos=="close":
               timenow=datetime.datetime.now()
               later=timenow+relativedelta(minutes=10)
               open_window(pos)
               gas_button=True
               text_gas_out="Indoor Mode - Gas Detected, Ventilates for 10 minutes"
               bot.send_message(chat_id=id, text=text_gas_out)
               bot.send_message(chat_id=id2, text=text_gas_out)
       present=datetime.datetime.now()
       if gas_button:
           if present>later:
               close_window(pos)
               gas_button=False
               text_gas_out_later="Indoor Mode - Gas, It's been 10 minutes, Closing the Window"
               bot.send_message(chat_id=id, text=text_gas_out_later)
               bot.send_message(chat_id=id2, text=text_gas_out_later)
       if PM10>50:
           if pos=="close":
               if PM10>PM10_outdoor:
                   if no_rain.is_active:
                       timenow=datetime.datetime.now()
                       later=timenow+relativedelta(minutes=10)
                       open_window(pos)
                       dust_button=True
                       text_dust_out="Indoor Mode - Indoor Dust exceeded 60㎍/m³, Ventilates for 10 minutes "
                       bot.send_message(chat_id=id, text=text_dust_out)
                       bot.send_message(chat_id=id2, text=text_dust_out)
       present=datetime.datetime.now()
       if dust_button:
           if present>later:
               close_window(pos)
               dust_button=False
               text_dust_out_later="Indoor Mode - Dust, It's been 10 minutes, Closing the Window"
               bot.send_message(chat_id=id, text=text_dust_out_later)
               bot.send_message(chat_id=id2, text=text_dust_out_later)
       if humi>70:
           if pos=="close":
               if no_rain.is_active:
                   if PM10_outdoor<=100:
                       timenow=datetime.datetime.now()
                       later=timenow+relativedelta(minutes=10)
                       open_window(pos)
                       humi_button=True
                       text_humi_out="Indoor Mode - Humidity exceeded 70%, Ventilates for 10 minutes"
                       bot.send_message(chat_id=id, text=text_humi_out)
                       bot.send_message(chat_id=id2, text=text_humi_out)
       present=datetime.datetime.now()
       if humi_button:
           if present>later:
               close_window(pos)
               humi_button=False
               text_humi_out_later="Indoor Mode - Humidity, It's been 10 minutes, Closing the Window"
               bot.send_message(chat_id=id, text=text_humi_out_later)
               bot.send_message(chat_id=id2, text=text_humi_out_later)
       if not no_rain.is_active:
           if pos == "open":
               if gasValue<= 400:
                   close_window(pos)
                   text_rain = "Indoor Mode - It's Raining, Shut down the Ventilation"
                   bot.send_message(chat_id=id, text=text_rain)
                   bot.send_message(chat_id=id2, text=text_rain)
                   humi_button=False
                   dust_button=False
                   gas_button=False
                   schedule_button=False
       if GPIO.input(20) == False:
           bot.send_message(chat_id=id, text="Detected Fire!\n")
           bot.send_message(chat_id=id2, text="Detected Fire!\n")
           camera.capture('fire' + '.jpg')
           bot.send_photo(chat_id=id, photo=open('/home/pi/Desktop/fire.jpg','rb'))
           bot.send_photo(chat_id=id2, photo=open('/home/pi/Desktop/fire.jpg','rb'))
           time.sleep(5)
       schedule.run_pending()
       present1=datetime.datetime.now()
       if schedule_button:
           if present1>later2:
               close_window(pos)
               schedule_button=False
               bot.send_message(chat_id=id, text="Ventilation is done")
               bot.send_message(chat_id=id2, text="Ventilation is done")
decode_data = ""
def recv_thread(client_socket):
   global decode_data
   while 1:
       data = client_socket.recv(1024)
       decode_data = data.decode("UTF-8")
       print(decode_data)
       time.sleep(2)
def handler(update, context):
   global decode_data
   decode_data=update.message.text
   dust_get()
   gasValue = analogRead(0)
   if decode_data=="status":
       bot.send_message(chat_id=id, text=("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%" .format(temp, humi)))
       bot.send_message(chat_id=id, text=("Gas =", gasValue))
       bot.send_message(chat_id=id, text=("PM0.1=",PM01,",PM10 = ",PM10,"PM25 =", PM25))
       bot.send_message(chat_id=id2, text=("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%" .format(temp, humi)))
       bot.send_message(chat_id=id2, text=("Gas = ",gasValue))
       bot.send_message(chat_id=id2, text=("PM0.1=",PM01,",PM10 = ",PM10,"PM25 =", PM25))
       #bot.send_message(chat_id=id, text=("습도 :{} %\n".format(humi),"온도 : {} *C".format(temp))) #"온도 : {} *C".format(temp))
   elif decode_data=="gate":
       if GPIO.input(reed)==0 or GPIO.input(reed1)==0:
           bot.send_message(chat_id=id, text="Window Plus is OPENED")
           bot.send_message(chat_id=id2, text="Window Plus is OPENED.")
       if GPIO.input(reed)==1 and GPIO.input(reed1)==1:
           bot.send_message(chat_id=id, text="Window Plus is CLOSED.")
           bot.send_message(chat_id=id2, text="Window Plus is CLOSED.")
   elif decode_data=="indoor":
       bot.send_message(chat_id=id, text="Indoor_mode is ongoing!")
       bot.send_message(chat_id=id2, text="Indoor_mode is ongoing!")
   elif decode_data=="outdoor":
       bot.send_message(chat_id=id, text="Outdoor_mode is ongoing!")
       bot.send_message(chat_id=id2, text="Outdoor_mode is ongoing!")
def handler_thread():
   while 1:
       echo_handler = MessageHandler(Filters.text, handler)
       dispatcher.add_handler(echo_handler)
       time.sleep(2)
def dust_gas_thread(client_socket):
   while 1:
       dust_get()
       gasValue = analogRead(0)
       gasValue_en=str(gasValue).encode("utf-8")
       PM10_en=str(PM10).encode("utf-8")
       PM25_en=str(PM25).encode("utf-8")
       aaa=","
       client_socket.send("999")
       client_socket.send(aaa)
       client_socket.send(PM10_en)
       client_socket.send(aaa)
       client_socket.send(gasValue_en)
       client_socket.send(aaa)
       client_socket.send(PM25_en)
       client_socket.send(aaa)
       client_socket.send("888")
       time.sleep(3)
setup()
recv_thread = threading.Thread(target=recv_thread, args=(client_socket, ), daemon=True)
dust_gas_thread = threading.Thread(target=dust_gas_thread, args=(client_socket, ), daemon=True)
outdoordust_thread =threading.Thread(target=outdoordust_thread, daemon=True)
handler_thread = threading.Thread(target=handler_thread, daemon=True)
handler_thread.start()
outdoordust_thread.start()
dust_gas_thread.start()
recv_thread.start()
while 1:
    pos=get_pos()
    if decode_data.find("open")==0:
            open_window(pos)
    elif decode_data.find("close")==0:
            close_window(pos)
    if decode_data.find("outdoor")==0:
            outdoor_button=True
            indoor_button=False
    elif decode_data.find("indoor")==0:
        indoor_button=True
        outdoor_button=False
    elif decode_data.find("open")==0:
        outdoor_button=False
        indoor_button=False
    elif decode_data.find("close")==0:
        indoor_button=False
        outdoor_button=False
    if outdoor_button:
        outdoor_mode()
    if indoor_button:
        indoor_mode()
    dht_11_send(client_socket)