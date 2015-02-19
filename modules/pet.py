import willie.module
from random import randint
from willie.formatting import bold

@willie.module.commands('pet')
def pet(bot, trigger):	
    """
    Pet command
    """
    x = randint(0,1) #inclusive

    if(x == 0):
        bot.say('Woof woof!')
    elif (x == 1):
        bot.action('wags his tail.')

