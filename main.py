import requests
import json
from flask import Flask, render_template
from urllib.request import urlopen
import math
import re
import json
import ipinfo
import pprint

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


with urlopen('https://discover.search.hereapi.com/v1/discover?at='+str(lat)+','+str(lon)+'&q=hospital&apiKey=N46AqYQ1bpAbqASUk_nsK-sMDNkFh5lkeAA2DFkPDU8') as resp:
	project_info = json.load(resp)#['title']
pprint.pprint(project_info)


p1title = project_info['items'][0]['title']

try:
    p1phone = project_info['items'][0]['contacts'][0]['phone'][0]['value']
except Exception:
    try:
        p1phone = project_info['items'][0]['contacts'][0]['mobile'][0]['value']
    except Exception:
        try:
            p1phone = "na"
        except Exception:
            pass

p1lat = project_info['items'][0]['access'][0]['lat']
p1lng = project_info['items'][0]['access'][0]['lng']


p1label = project_info['items'][0]['address']['label']


p2title = project_info['items'][1]['title']
try:
    p2phone = project_info['items'][1]['contacts'][0]['phone'][0]['value']
except Exception:
    try:
        p2phone = project_info['items'][1]['contacts'][0]['mobile'][0]['value']
    except Exception:
        try:
            p2phone = "na"
        except Exception:
            pass

p2lat = project_info['items'][1]['access'][0]['lat']
p2lng = project_info['items'][1]['access'][0]['lng']

p3title = project_info['items'][2]['title']
try:
    p3phone = project_info['items'][2]['contacts'][0]['phone'][0]['value']
except Exception:
    try:
        p3phone = project_info['items'][2]['contacts'][0]['mobile'][0]['value']
    except Exception:
        try:
            p3phone = "na"
        except Exception:
            pass
p3lat = project_info['items'][2]['access'][0]['lat']
p3lng = project_info['items'][2]['access'][0]['lng']

p4title = project_info['items'][3]['title']
try:
    p4phone = project_info['items'][3]['contacts'][0]['phone'][0]['value']
except Exception:
    try:
        p4phone = project_info['items'][3]['contacts'][0]['mobile'][0]['value']
    except Exception:
        try:
            p4phone = "na"
        except Exception:
            pass
p4lat = project_info['items'][3]['access'][0]['lat']
p4lng = project_info['items'][3]['access'][0]['lng']

p5title = project_info['items'][4]['title']
try:
    p5phone = project_info['items'][4]['contacts'][0]['phone'][0]['value']
except Exception:
    try:
        p5phone = project_info['items'][4]['contacts'][0]['mobile'][0]['value']
    except Exception:
        try:
            p5phone = "na"
        except Exception:
            pass

p5lat = project_info['items'][4]['access'][0]['lat']
p5lng = project_info['items'][4]['access'][0]['lng']

p6title = project_info['items'][5]['title']
try:
    p6phone = project_info['items'][5]['contacts'][0]['phone'][0]['value']
except Exception:
    try:
        p6phone = project_info['items'][5]['contacts'][0]['mobile'][0]['value']
    except Exception:
        try:
            p6phone = "na"
        except Exception:
            pass
p6lat = project_info['items'][5]['access'][0]['lat']
p6lng = project_info['items'][5]['access'][0]['lng']


app = Flask(__name__)
 
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return render_template('landing.html')
    #return redirect('https://1.base.maps.ls.hereapi.com/maptile/2.1/maptile/newest/normal.day/13/'+str(int(xTile))+'/'+str(int(yTile))+'/512/png8?apiKey=N46AqYQ1bpAbqASUk_nsK-sMDNkFh5lkeAA2DFkPDU8', code=302)

@app.route('/vmd_timestamp')
def vmd_timestamp():
	data = {'x': float(lat), 'y': float(lon), 'p1title': p1title , 'p1phone': p1phone, "p1lat": float(p1lat), "p1lng": float(p1lng), "p1label": p1label, 'p2title': p2title , 'p2phone': p2phone, "p2lat": float(p2lat), "p2lng": float(p2lng), 'p3title': p3title , 'p3phone': p3phone, "p3lat": float(p3lat), "p3lng": float(p3lng), 'p4title': p4title , 'p4phone': p4phone, "p4lat": float(p4lat), "p4lng": float(p4lng), 'p5title': p5title , 'p5phone': p5phone, "p5lat": float(p5lat), "p5lng": float(p5lng), 'p6title': p6title , 'p6phone': p6phone, "p6lat": float(p6lat), "p6lng": float(p6lng)}
	return render_template('vmd_timestamp.html', data=data)
		
if __name__ == '__main__':
 
    # run() Flask application on local server.
    app.run()