# Python program to find current  
# weather details of any city 
# using openweathermap api 
  
# import required modules 
import requests, json 
  
# Enter your API key here 
api_key = "c08a166434e6b3103a0009cd0dd59d23"
  
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
    #name = x["name"]
  
    # print following values 

    print(" City name: " + city_name+
	  "\n Temperature (in kelvin unit) : " +
                    str(current_temperature) + ", (in Celsius unit) : " + str(C_degree) + 
	  "\n Minimum temperature : " + str(min_temp) +
	  "\n Maximum temperature : " + str(max_temp) +
          "\n Atmospheric pressure (in hPa unit) : " +
                    str(current_pressure) +
          "\n Humidity (in percentage) : " +
                    str(current_humidiy) +
          "\n Description : " +
                    str(weather_description)) 
  
else: 
    print(" City Not Found ") 