import willie.module
from random import randint

@willie.module.commands('sniffbutt')
def sniffbutt(bot, trigger):
    """
    sniffbutt [object] - tells Frisket to sniff the commander's butt
    """
    x = randint(0,10) #inclusive

    bot.action('sniffs {}\'s butt.'.format(trigger.nick))
    if(x < 7):
        bot.say('Smells like a friendly butt! Woof!')
    elif(x >= 8 and x <= 10):
        bot.say('Smells bad! You\'re not a friend of mine! Angry Woof!')
