# -*- coding: utf-8 -*-
"""
games.py - Game framework for Willie

This module deals with core requirements of IRC games. It handles
command recognition, registration, and keeping track of scores.
"""

from __future__ import unicode_literals
from __future__ import print_function

import willie.module

#TODO: set in 'configure' function
command_prefix = '!'

@willie.module.rule('^' + command_prefix + '.*')
def start_game(bot, trigger):
    pass

