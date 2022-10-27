#앱에서 데이터 받음.
decode_data = ""
def recv_thread(client_socket):
   global decode_data
   while 1:
       data = client_socket.recv(1024)
       decode_data = data.decode("UTF-8")
       print(decode_data)
       time.sleep(2)
recv_thread = threading.Thread(target=recv_thread, args=(client_socket, ), daemon=True)
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
