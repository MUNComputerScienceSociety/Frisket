import willie.module
import re
from random import randint

count = 0		#get tired after some time
hungry = False

@willie.module.commands('throw')
@willie.module.commands('fetch')
@willie.module.rule('throw?')
@willie.module.rule('fetch?')
def throwcommand(bot, trigger):	
	global count
	global hungry

	if(hungry == True):
		bot.action('can\'t do anything until fed!')
	else:
		x = randint(0,5)	#inclusive
		words = re.split(' ' , trigger)
		del words[0]
		joined_words = ' '.join(words)
		
		if( x < 4):
			if count == 3:
				bot.action('Tired')
				count = 0
			else:
				bot.action('chases after ' + joined_words)
				count = count + 1
		elif (x == 4):
			bot.action('didn\'t see the ' + joined_words + ', chases squirrel instead')
		elif (x == 5):
			bot.action('is hungry!!! (dont want to fetch)')
			hungry = True


@willie.module.rule('feed')
def welcome(bot, trigger):
	global hungry
	bot.action('woof woof!')
	hungry = False
	
