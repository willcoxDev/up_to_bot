Just made this as a prrof of concept. Will not be updating it further.

If you want to use yourself

Install python, and praw (reddits api)

Open the config file
Insert your bots
username, password, client_id and client_secret
Save the config file.

Open up_to_bot.py

Change user_agent to your bots name and its reddit username 
(tells reddit a description each time the api is called)

Change the following variables to where the 
three revlevant text files are located on your system.
found_text, notfound_text and correct_text

Save up_to_bot.py

Shift right click the containing folder and 'open command prompt here'
type: py up_to_bot.py
The bot should run now until you stop it (ctrl + c)

Bugs you may run into:

If your bot gets banned from a subreddit and it attempts to post to that sub again
you will get an exception and the bot will stop working.

If you decide to use notfound_text the list will get massive and slow down the bot by
a very noticable amount. I personally have commented out all areas that use it.
