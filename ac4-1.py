#!/usr/bin/env python3

from time import sleep
import sys
import http.client
import urllib.request
import random

random.seed()
chave = 'EHVPSN3DJPHDV3KS'
base_url = f'https://api.thingspeak.com/update?api_key={chave}'

while True:
    valor = random.randint(0, 100)
    conn = urllib.request.urlopen(base_url + '&field1=' + str(valor))
    print(conn.read())
    print('Valor enviado: ' + str(valor))
    conn.close()
    sleep(10)