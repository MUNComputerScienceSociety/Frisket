import willie.module
import re
from random import randint

count = randint(2,5)		#get tired after some time (randomized)
hungry = False


@willie.module.commands('throw')
@willie.module.commands('fetch')
@willie.module.rule('throw?')
@willie.module.rule('fetch?')
def throwcommand(bot, trigger):	
	global count
	global hungry

	if(hungry == True):
		HungryMessage(bot)
		return
	
	x = randint(0,5)	#inclusive
	words = re.split(' ' , trigger)
	del words[0]
	joined_words = ' '.join(words)

	if count == 0:
		bot.action('Tired')
		Tired(bot, trigger)
	elif(x < 3):
		bot.action('chases after ' + joined_words)
		count -= 1
	elif (x == 3):
		Rest(bot, trigger)
	elif (x == 4):
		bot.action('didn\'t see the ' + joined_words + ', chases squirrel instead')
		count -= 1
	elif (x == 5):
		bot.action('is hungry!!! (dont want to fetch)')
		hungry = True


@willie.module.rule('feed')
def Feed(bot, trigger):
	global hungry
	bot.action('woof woof!')
	hungry = False
	
def HungryMessage(bot):
	bot.action('can\'t do anything until fed!')

def Tired(bot, trigger):
	global count
	bot.action('Sleepy')
	Rest(bot, trigger)
	count = randint(2,5)

@willie.module.rule('rest')
@willie.module.rule('sleep')
def Rest(bot, trigger):
	global count
	bot.action('zzzzzzzzzz!!!!')
	count = randint(2,5)

@willie.module.rule('pets')
def Pets(bot, trigger):
	bot.action('woooof wooooof')


