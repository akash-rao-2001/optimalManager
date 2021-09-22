import requests
import json
from flask import Flask,redirect
import urllib.request

#response = requests.get("https://image.maps.ls.hereapi.com/mia/1.6/mapview?apiKey=N46AqYQ1bpAbqASUk_nsK-sMDNkFh5lkeAA2DFkPDU8")
#print(response.json())


app = Flask(__name__)
 
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return redirect('https://1.base.maps.ls.hereapi.com/maptile/2.1/maptile/newest/normal.day/13/4400/2686/256/png8?apiKey=N46AqYQ1bpAbqASUk_nsK-sMDNkFh5lkeAA2DFkPDU8', code=302)

if __name__ == '__main__':
 
    # run() Flask application on local server.
    app.run()