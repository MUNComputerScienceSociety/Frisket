import willie.module
import re
from random import randint

count = 0		#get tired after some time

@willie.module.commands('throw')
@willie.module.commands('fetch')
@willie.module.rule('throw?')
@willie.module.rule('fetch?')
def throwcommand(bot, trigger):	
	global count

	x = randint(0,5)	#inclusive
	words = re.split(' ' , trigger)
	del words[0]
	joined_words = ' '.join(words)

	if( x < 3):
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
	
		
