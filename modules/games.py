# -*- coding: utf-8 -*-
"""
games.py - Game framework for Willie

This module deals with core requirements of IRC games. It handles
command recognition, registration, and keeping track of scores.
"""

from __future__ import unicode_literals
from __future__ import print_function

import willie.module
from willie.formatting import bold

#TODO: set in 'configure' function
command_prefix = '!'
game_channels = ['#muncs-games', '#mainframe']


@willie.module.rule('^' + command_prefix + 'game\s(\w*)')
def start_game(bot, trigger):
    if trigger.is_privmsg:
        bot.reply("This command only works in channels")
        return
    elif not trigger.sender in game_channels:
        bot.reply("Games are not allowed in this channel")
        return
    elif trigger.sender in bot.memory and 'current_game' in bot.memory[trigger.sender]:
        bot.reply("Cannot start game; already one running: " + bot.memory[trigger.sender]['current_game'])
        return
    
    bot.say(bold('WARNING:') + " Incoming game")
    bot.say("Starting " + trigger.group(1))
    
    bot.memory[trigger.sender] = {'current_game': trigger.group(1)}
    
    return
