#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8148675085:AAF0ZagvhBh7GhOtsJ19fhyRcl4L1e582cY")
    API_ID = int(os.environ.get("API_ID", "22537641"))
    API_HASH = os.environ.get("API_HASH", "6c1eee32be959812f0598919209a2105")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6748247898")
