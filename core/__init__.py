# modules needed to run this bot

from flask import Flask,render_template,request
import requests,os,json



# configuration
token = os.environ['TOKEN'] # dont remove this 
my_url = 'https://api.telegram.org/bot1351102221:AAH-RVuQKzF0-XRIrZckxe0BgQwjUEuyHxQ'
bot_token = 'bot1351102221:AAH-RVuQKzF0-XRIrZckxe0BgQwjUEuyHxQ'
app = Flask(__name__)
