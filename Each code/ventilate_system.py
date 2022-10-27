#외부 우천,미세먼지 수치를 확인 후 정해진 시간에 10분간 환기를 진행.
#후에 실내,실외 모드에서 적용
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
