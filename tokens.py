import os

# Set your api tokens and proxy through environmental variables
# (add lines to your .bashrc and restart terminal):
# export BOT_TOKEN='XXXXX:XXXXXXXXXXX'

token = os.getenv('BOT_TOKEN')
assert token is not None, 'Problem in reading BOT_TOKEN variable. Read tokens.py for information'
