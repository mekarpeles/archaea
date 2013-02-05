# -*- coding: utf-8 -*-
"""
    config.py
    ~~~~~~~~~
    This module is the middle man for handling/consolidating
    configurations for the documentation server.

    :copyright: (c) 2012 by Mek
    :license: BSD, see LICENSE for more details.
"""

import os
import ConfigParser

config = ConfigParser.ConfigParser()
cfg = 'configs/archaea.cfg'
debug_mode = False
dbname = 'archaea'
if os.path.isfile(cfg):
    config.read(cfg)
    try:
        dbname = config.get("db", "name")
    except:
        pass
    try:
        debug_mode = bool(config.get("server", "debug"))
    except:
        pass
        
SERVER = {'DEBUG_MODE': debug_mode}
DBNAME = dbname 
