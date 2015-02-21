# -*- coding: utf-8 -*-
import willie.module
import willie.web
import json
from willie.formatting import bold

@willie.module.commands('munweather')
def munweather(bot, trigger):	
    """
    munweather - gets the bot to tell you the current weather at the nearest weather station to the
    MUN Engineering building coordinates. weather data is retrieved from the Open Weather API.
    """

    url = "http://api.openweathermap.org/data/2.5/weather?lat=47.574037&lon=-52.734607"

    # parse json into a python dict
    data = json.loads(willie.web.get(url))
    # get string description and current temperature in Celsius
    description = data['weather'][0]['description']
    temp = data['main']['temp'] - 273.15
    # get humidity and wind speed in km/h
    humidity = data['main']['humidity']
    windspeed = data['wind']['speed'] * 3.6

    answer = "The current weather is {}! It is {:.1f}\N{DEGREE SIGN}C ".format(description,
            temp)
    if(temp < -5):
        answer += "cold! Brrr!"
    elif(temp >= -5 and temp < 5):
        answer += "chilly!"
    elif(temp >= 5 and temp < 20):
        answer += "! Rather pleasant!"
    elif(temp >= 20 and temp < 25):
        answer += " warm!"
    else:
        answer += " hot!"

    answer2 = "The humidity is {}% and the wind speed is {:.1f} km/h.".format(humidity, windspeed) 

    bot.say(answer)
    bot.say(answer2)
    bot.say(bold("Woof!")) 
