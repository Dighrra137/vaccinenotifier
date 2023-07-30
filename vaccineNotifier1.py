import requests
import time
import json
from datetime import datetime, timedelta

personAge = 67
pinCode = ['211001']
totalDays = 1
printFlag = 'Y'

print("Start searching for covid vaccine slots :")

current = datetime.today()
form  = [current + timedelta(days=i) for i in range(totalDays)]
correctDate = [i.strftime("%d-%m-%y") for i in form]

while True:
    i = 0
    for findCode in pinCode:
        for enterDate in correctDate:
            
            url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(findCode, enterDate)
                
            requirements = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
            }
            finalOP = requests.get(url,headers=requirements)
            
            if finalOP.ok:
               fileJSON = finalOP.json()
               
               flag = False
               for place in fileJSON["centers"]:
                        for availability in place["sessions"]:
                            if(availability['min_age_limit']<=personAge and availability["available_capacity"]>0):
                                print("The pincode for which you're searching for:",findCode)
                                print("It is available on : {}".format(enterDate))
                                print("Name of the vaccine center and destination:",place["name"])
                                print("Name for the block is :",place["block_name"])
                                print("Price for the vaccine is :",place["fee_type"])
                                print("Availability status :",availability["available_capacity"],"\n")
                                
                                if(availability["vaccine"]!=''):
                                  print('The type of the vaccine is',availability['vaccine'])
                                i = i+1
                            else:
                                pass
            else:
                print("I found no response !!!.......")
    
    if i==0:
       print("Right now no vaccine slots are available !...Try after some time")
    else:
       print("The search is finished !")
    
    dateNow = datetime.now() + timedelta(minutes=1)
    
    while datetime.now() < dateNow:
        time.sleep(1)
        
        
        
        
        
        
        
        
        
        
        
        
        # copied successfully!!





        