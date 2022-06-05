def main():
  print("Welcome!")

main()

import json, requests

base_url= "https://api.openweathermap.org/data/2.5/weather"
appid= "38c55011d6ce4d19408075a3eb62c37d"
city= input("Enter your city: ")

url= f"{base_url}?q={city}&units=imperial&APPID={appid}"
print(url)
print()

response= requests.get(url)
unformated_data= response.json()
#print(unformated_data)
if response.json()['cod'] == '404' :
  print("No city found")
else:
  #create variables to store and display data
  temp= unformated_data["main"]["temp"]
  print(f"The current temp is: {temp} °F")
  temp_min= unformated_data["main"]["temp_min"]
  print(f"The min temp is: {temp_min}°F")
  temp_max= unformated_data["main"]["temp_max"]
  print(f"The max temp is: {temp_max}°F")
  weather_desc= unformated_data["weather"][0]["description"]
  print(f"The current weather desc is: {weather_desc}")
  


