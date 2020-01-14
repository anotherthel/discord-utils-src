from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return 'Wrong place. Go to discord to interact with bot.'

def run():
  app.run(host='0.0.0.0',port=1742)

def keep_alive():  
    t = Thread(target=run)
    t.start()
