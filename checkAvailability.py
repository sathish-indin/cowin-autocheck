import json
import sys,getopt
import requests
import time

def main(argv):
 pincode=''
 vaccine=''
 date=''
 age=''
  
 while True:

  try:
   opts, args=getopt.getopt(argv,"p:v:d:a:",['pincode=','vaccine=,"date=","age='])
  except getopt.GetoptError:
   print('checkAvailability.py -p <pincode> -v <vaccine> -d <date in dd/mm/yy> -a <18 for 18+ and 45 for 45+>')
   sys.exit(2)
  for opt,arg in opts:
   if opt == '-p':
    pincode=arg
   elif opt == '-v':
    vaccine=arg
   elif opt == '-d':
    date=arg
   elif opt == '-a':
    age=arg

  uri="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+pincode+"&date="+date
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'} 
  response=requests.get(uri,headers=headers)
  centers_json= response.json()

  #centers_json = json.loads(test_json)

  for i in centers_json['centers']:
   if str(i["pincode"]) in pincode:
    for j in i["sessions"]:
       if j["vaccine"] == vaccine and j["available_capacity"] > 0 and j["min_age_limit"] == int(age) : 
         print ("available_capacity :", j["available_capacity"] , " date :"+j["date"] ," center :"+i["name"])

  time.sleep(60);
if __name__ == "__main__":
  main(sys.argv[1:])
