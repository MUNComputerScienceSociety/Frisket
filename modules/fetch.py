import willie.module
import re
from random import randint
from willie.formatting import bold

@willie.module.commands('throw')
@willie.module.commands('fetch')
def fetch(bot, trigger):	
    """
    fetch [object] - tells Frisket to fetch the object
    """
    x = randint(0,10) #inclusive
    words = re.split(' ' , trigger)
    del words[0]
    joined_words = ' '.join(words)

    if(x < 5):
        bot.action('fetches the ' + bold(joined_words) + ' for ' + trigger.nick)
    elif(x >= 5 and x < 10):
        bot.action('brings the ' + bold(joined_words) + ' back to ' + trigger.nick)
    elif (x == 10):
        bot.action('ignores ' + trigger.nick + ' and chases a squirrel instead')

