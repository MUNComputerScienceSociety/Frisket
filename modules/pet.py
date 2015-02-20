import willie.module
from random import randint

@willie.module.commands('pet')
def pet(bot, trigger):	
    """
    pet - Pets Frisket
    """
    x = randint(0,1) #inclusive

    if(x == 0):
        bot.say('Woof woof!')
    elif (x == 1):
        bot.action('wags his tail.')

