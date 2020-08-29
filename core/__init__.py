# modules needed to run this bot

from flask import Flask,render_template,request
import requests,os,json



# configuration
token = os.environ['TOKEN'] # dont remove this 
my_url = 'https://api.telegram.org/bottoken'
bot_token = 'bottoken'
app = Flask(__name__)
