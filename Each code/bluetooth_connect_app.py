import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓 생성
sock.connect(("pwnbit.kr", 443))
ip=sock.getsockname()[0]
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
port = 1                                                    
server_socket.bind(("",port))                               #bind 함수로 지정된 포트에 연결
server_socket.listen(1)                                     #listen 함수로 클라이언트 대기 상태
client_socket,address = server_socket.accept()              #accept 클라이언트 요청 시 연결
print("Accepted connection from ", address)
