#!/bin/bash
# This script restarts python nicebot process

ps aux | grep -v grep | grep nicebot.py | awk '{ print $2 }' | xargs kill -9
python ~centos/nicetelebot/nicebot.py >> ~centos/nicetelebot/bot.log 2>&1 &


