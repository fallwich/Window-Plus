#실내모드 -실외모드의 기능에서 침입자 감지가 빠짐.
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