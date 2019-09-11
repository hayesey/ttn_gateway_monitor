#!/usr/bin/python3
import settings
import requests
import datetime
import sys

data = {}

session = requests.Session()

try:
    if sys.argv[1] == 'debug':
        debug = True
    else:
        debug = False
except:
    debug = False

for this_eui in settings.gw_euis:
    if not this_eui.startswith('eui-'):
        gw_id = "eui-{}".format(this_eui)
    else:
        gw_id = this_eui

    gw_data = session.get('http://noc.thethingsnetwork.org:8085/api/v2/gateways/{}'.format(gw_id)).json()
    date_time_obj = datetime.datetime.strptime(gw_data['timestamp'].split('.')[0], '%Y-%m-%dT%H:%M:%S')
    mins = int((datetime.datetime.utcnow().timestamp() - date_time_obj.timestamp())/60)
    data[this_eui] = mins

if debug:
    print("Data: {}".format(data))
    
result = requests.post('https://push.nodeping.com/v1', params={'id': settings.nodeping_id, 'checktoken': settings.nodeping_token}, json={'data': data}, headers={'Content-Type': 'application/json'})

if debug:
    print("Nodeping result: {}".format(result.content))
