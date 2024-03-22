# twitchBot

## PLANS FOR FUTURE 
I'm writing this so I can see this for myself in the future and actually make changes --
I started this project on the newest version of Python, but all the documentation is for the older versions, and I was still such a coding beginner before that I didn't realize I could just use a Python version manager and write my code in old Python versions. I'm gonna revamp this whole thing at some point and try to make this a fully functional bot for my Twitch chat with a bunch of fun features that someone else could possibly use too. For now though, I have other stuff to do. Written as of 3/22/24. Will try to start in May once I get free time from this semester.

### What this is for

This is meant to be used for my own personal Twitch stream chat. Others can of course look at the code and copy it or
install it in order to modify it and make their own Twitch chat-bot.

This was also meant to be used as practice in Python, since I figured it would be useful to try and get used to what the
language entails.

### What the bot can do

The bot can, as of right now, read and write basic messages to chat.

I've included basic functions like .twitter, .discord, and .grindserver, with the idea being that they could link to my
social media page, my personal Discord server, and my fighting game specific Discord server respectively. The links are
held through key:value pairs in dictionary `dynamic_variables`, with the key being the command people in chat type in
and the value being the link itself. 

The key:value pairs are also stored in a personal `outputs.txt` file which I have
saved in the project (not in the remote repository). The idea is that since I don't have a way to run the bot 24/7, if
I were to use this bot I could simply store it in a .txt file that can change dynamically while the program is run
without me needing to edit `main.py` or the code directly, instead using Twitch chat commands like `.editcom 
.commandName [editToBeMade]`.

### TBA 

The add, edit, and remove command functions are currently being worked on. This is a bit of a personal tangent, but I
have not worked with Python at this level at all nor have I worked with Python in a while, so I'm spending time trying
to understand how everything works -- like the decorators and their influence on code (especially because it is very
different in Java, as to my knowledge Java decorators are purely for readers), what pipenv is, etc. -- to a level where
I won't need to constantly circle back to documentation to try understanding it.

The edit, add, and remove command functionality is about halfway complete.

### Future ideas for the bot

I think it would be really fun if I could have a way to do song requests through the bot that link directly to either
a YouTube playlist or Google Chrome so that I could have viewers type something like `.sr [YT link]` and it would
directly influence the song I am listening to without needing to click links or anything. I might need to use some
YouTube APIs or something for that, but that will come after I can edit commands.
