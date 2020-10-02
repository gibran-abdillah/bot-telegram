# modules needed to run this bot

from flask import Flask,render_template,request
import requests,os,json



# configuration
token = os.environ['TOKEN'] # dont remove this 
my_url = 'https://api.telegram.org/1346881100:AAEf2ahZ2C6CbczPf_Ul95DRvW4Fi6_WnGw' # change 'bottoken' with your token
bot_token = '1346881100:AAEf2ahZ2C6CbczPf_Ul95DRvW4Fi6_WnGw' # change this to
app = Flask(__name__)
