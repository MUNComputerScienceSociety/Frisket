from willie import module
import re

@module.commands('throw')
@module.commands('fetch')
@module.rule('throw?')
@module.rule('fetch?')
def throwcommand(bot, trigger):
	words = re.split(' ' , trigger)
	del words[0]
	a = ' '.join(words)
	bot.say(bot.nick + ' chases after ' + a)
	
