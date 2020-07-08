#!/bin/bash

git add *
git commit -m "$1"
git push heroku master
heroku run python3 bot.py
bash