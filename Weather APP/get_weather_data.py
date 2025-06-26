import requests

city_name = input("Enter the City Name: ")
api_key = ""        # Get the api from "www.openweathermap.org/api" and paste your api here
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

response = requests.get(url)
'''
A status code 200 in HTTP indicates that the server has successfully processed the client’s request and is returning the requested content in the response body.
'''
if(response.status_code==200):
    print("Connection Sucessfull!!!")
    data = response.json()
    # This prints whole data coming from the API
    print(data)
    print("------------------")
    # This prints whole data of a list named weather
    print(data['weather'])
    # This prints a specific index of the list which is a dictionary
    print(data['weather'][0])
    # This prints a key value of dictionary inside the weather list description, it tells us about the condition of the weather
    print("Weather Condition is: ",data['weather'][0]['description'])

    # now printing tempreture
    print('Current Tempreture is: ', data['main']['temp'])
    print('Current Tempreture Feels Like: ', data['main']['feels_like'])
    print("Minimum Tempreture is: ", data['main']['temp_min'])
    print("Maximum Tempreture is: ", data['main']['temp_max'])
    print("Pressure is: ", data['main']['pressure'])
    print("Clouds are: ", data['clouds']['all'])
    print("Visibility is: ", data['visibility'])
    print("Humidity is: ", data['main']['humidity'])
    print("Wind Speed is: ", data['wind']['speed'])
else:
    print("You might not wrote the correct city name, Try Again!!!")