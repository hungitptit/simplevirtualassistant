# Python program to find current  
# weather details of any city 
# using openweathermap api 
import sys  
# import required modules 
import requests, json 
import pyttsx3
from googletrans import Translator
# Enter your API key here 
api_key = "c08a166434e6b3103a0009cd0dd59d23"
vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
robot_mouth = pyttsx3.init()
robot_mouth.setProperty('voice', vi_voice_id)
translator = Translator()
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name 
city_name = "Hanoi"
  
# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  
# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json()
#print(x) 
  
# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 
  
    # store the value of "main" 
    # key in variable y 
    y = x["main"] 
  
    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"] 
    C_degree = current_temperature-273.15
    min_temp = y["temp_min"]-273.15
    max_temp = y["temp_max"]-273.15
    # store the value corresponding 
    # to the "pressure" key of y 
    current_pressure = y["pressure"] 
  
    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 
  
    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 
  
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
    weather_description = z[0]["description"] 
    mota = translator.translate(weather_description , dest='vi').text 
    #name = x["name"]
  
    # print following values 
    
    
    #translator.translate('안녕하세요.')
    #<Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
  
    srcText = " Tên thành phố: " + city_name + "\n Nhiệt độ (tính theo độ K) : " +str(current_temperature) + ", (tính theo độ C) : " + str(C_degree) + "\n Nhiệt độ thấp nhất : " + str(min_temp) + " độ C"+"\n Nhiệt độ cao nhất : " + str(max_temp) +" độ C"+"\n Áp suất không khí (tính theo hPa) : " +str(current_pressure) +"\n Độ ẩm (tính theo phần trăm) : " +str(current_humidiy) +"\n Mô tả: " +str(mota) + " ("+weather_description+")"
    
    
    print(srcText)
    robot_mouth.say(srcText)
    robot_mouth.runAndWait()
    
  
else: 
    print(" City Not Found ") 