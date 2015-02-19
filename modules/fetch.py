import willie.module
import re
from random import randint
from willie.formatting import bold

@willie.module.commands('throw')
@willie.module.commands('fetch')
def fetch(bot, trigger):	
    """
    Fetch command
    """
    x = randint(0,9) #inclusive
    words = re.split(' ' , trigger)
    del words[0]
    joined_words = ' '.join(words)

    if(x < 5):
        bot.action('fetches ' + joined_words + ' for ' + bold(trigger.nick))
    elif(x >= 5 and x < 9):
        bot.action('chases after ' + joined_words)
    elif (x == 9):
        bot.action('didn\'t see the ' + joined_words + ', chases squirrel instead')

