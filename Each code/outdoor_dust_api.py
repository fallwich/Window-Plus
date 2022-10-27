#공공데이터포털에서 미세먼지 수치를 받아온다.
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
         if decode_data in stationName: #앱이나 telegram으로 지역을 받아와 그 지역에 대한 미세먼지 값 추출
             station_find=stationName.index(decode_data)
             print("staion:", stationName[station_find],"pm10:", pm10Value[station_find],"pm25:", pm25Value[station_find])
             PM10_outdoor=int(pm10Value[station_find])
             time.sleep(10)
