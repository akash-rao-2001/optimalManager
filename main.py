import requests
import json
from flask import Flask, render_template
import urllib.request
import math
import re
import json
import ipinfo

access_token = '418fa716a075cf'
handler = ipinfo.getHandler(access_token)
details = handler.getDetails()

d = details.loc.split(",")


lat_py = float(d[0])
lon_py = float(d[1])
print(lat_py, lon_py)
lat = lat_py #lattitude
lon = lon_py #longitude
z = 13 		 #zoom
latRad = lat * math.pi / 180
n = pow(2, z)
xTile = n * ((lon + 180) / 360)
yTile = n * (1-(math.log(math.tan(latRad) + 1/math.cos(latRad)) /math.pi)) / 2


app = Flask(__name__)
 
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	data = {'x': float(lat), 'y': float(lon)}
	return render_template('index.html', data=data)
    #return redirect('https://1.base.maps.ls.hereapi.com/maptile/2.1/maptile/newest/normal.day/13/'+str(int(xTile))+'/'+str(int(yTile))+'/512/png8?apiKey=N46AqYQ1bpAbqASUk_nsK-sMDNkFh5lkeAA2DFkPDU8', code=302)

if __name__ == '__main__':
 
    # run() Flask application on local server.
    app.run()