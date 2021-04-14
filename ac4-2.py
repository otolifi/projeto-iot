#!/usr/bin/env python3

from time import sleep
import urllib2
import urllib
import random

random.seed()
chave = 'FPB4YVYYLT05C38C'
base_url = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update'


while True:
    valor = random.randint(0, 5)
    if valor == 1:
        data = urllib.urlencode({'api_key': chave, 'status': 'A casa foi invadida!'})
        response = urllib2.urlopen(url=base_url, data=data)
    sleep(20)