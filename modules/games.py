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
game_channels = ['#muncs-games', '#mainframe', '#gamecube']
valid_games = ['rockpapersissors']

@willie.module.rule('^' + command_prefix + 'start\s(\w+)')
def start_game(bot, trigger):
    if trigger.is_privmsg:
        bot.reply("This command only works in channels")
        return
    elif not trigger.sender in game_channels:
        bot.reply("Games are not allowed in this channel")
        return
    elif 'game' in bot.memory and trigger.sender in bot.memory['game']:
        bot.reply("Cannot start game; already one running: " + bot.memory['game'][trigger.sender]['current_game'])
        return
    
    bot.say(bold('WARNING:') + " Incoming game")
    bot.say("Starting " + trigger.group(1))
    
    if not 'game' in bot.memory:
        bot.memory['game'] = {}
    
    bot.memory['game'][trigger.sender] = {'current_game': trigger.group(1)}
    
    return


@willie.module.rule('^' + command_prefix + 'end')
def end_game(bot, trigger):
    if trigger.is_privmsg:
        bot.reply("This command only works in channels")
        return
    elif not 'game' in bot.memory or not trigger.sender in bot.memory['game']:
        bot.reply("There is no current game to end")
        return
    
    bot.say("Game over")
    
    del bot.memory['game'][trigger.sender]
    
    return
