import willie.module
import re

count = 0		#get tired after some time

@willie.module.commands('throw')
@willie.module.commands('fetch')
@willie.module.rule('throw?')
@willie.module.rule('fetch?')
def throwcommand(bot, trigger):
	global count
	if count == 3:
		bot.action('Tired')
		count = 0	
	else:
		words = re.split(' ' , trigger)
		del words[0]
		joined_words = ' '.join(words)
		bot.action(' chases after ' + joined_words)
		count = count + 1
