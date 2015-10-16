# -*- coding: utf-8 -*-
import willie.module
import urllib2
import json
from willie.formatting import bold

API_KEY = 'put forecast.io API key here'

@willie.module.commands('munweather')
def munweather(bot, trigger):
    """
    munweather - gets the bot to tell you the current weather at the nearest weather station to the
    MUN Engineering building coordinates. Weather data is retrieved from The Dark Sky Forecast API.
    """

    url = 'https://api.forecast.io/forecast/{}/47.574037,-52.734607?units=ca'.format(API_KEY)

    response = urllib2.urlopen(url)
    if response.getcode() != 200:
        bot.say('There is no weather at MUN! :O')
        return
    data = json.load(response)

    description = data['currently']['summary']
    temp = data['currently']['temperature']
    humidity = data['currently']['humidity'] * 100
    windspeed = data['currently']['windSpeed']
    precip_probability = data['currently']['precipProbability'] * 100

    answer = 'The current weather is {}! It is {:.1f}\N{DEGREE SIGN}C '.format(description, temp)
    if(temp < -5):
        answer += 'cold! Brrr!'
    elif(temp >= -5 and temp < 5):
        answer += 'chilly!'
    elif(temp >= 5 and temp < 20):
        answer += '! Rather pleasant!'
    elif(temp >= 20 and temp < 25):
        answer += 'warm!'
    else:
        answer += 'hot!'

    answer2 = 'The humidity is {}% and the wind speed is {:.1f} km/h.'.format(humidity, windspeed)
    answer2 += ' The probability of precipitation is {}%!'.format(precip_probability)

    bot.say(answer)
    bot.say(answer2)
    bot.say(bold('Woof!'))
