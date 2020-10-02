# modules needed to run this bot

from flask import Flask,render_template,request
import requests,os,json



# configuration
token = os.environ['TOKEN'] # dont remove this 
my_url = 'https://api.telegram.org/bottoken' # change 'bottoken' with your token
bot_token = 'bottoken' # change this to
app = Flask(__name__)
