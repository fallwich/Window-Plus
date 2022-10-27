#telegram 챗봇을 이용해 창문을 제어. gate, status, open, close, indoor, outdoor, 지역 이름 키워드를 이용해 제어.
token = "5450872980:AAFGO1EWbbJyFJcNcopkc3mEGnsxdf5PZiA"
id="5623439502"
id2="5350738571"
bot = telegram.Bot(token=token)
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()
def handler(update, context):
   global decode_data #앱에서 받아오는 데이터 값과 같은 변수로 두어 같이 제어 가능.
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
handler_thread = threading.Thread(target=handler_thread, daemon=True)
handler_thread.start()