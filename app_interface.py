#모바일 앱 인터페이스에 실내 환경을 표시 (온도,습도,미세먼지,가스)
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
def dust_gas(client_socket):
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