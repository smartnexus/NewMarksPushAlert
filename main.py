import requests 
from dateutil.parser import parse as parsedate
from datetime import date

URL = "http://trajano.us.es/docencia/EstructuraYProtocolosDeRedesPublicas/"

r = requests.get(url = URL) 
  
last_modified = r.headers['Last-Modified']
http_date = parsedate(last_modified).strftime('%Y-%m-%d')
now = date.today()

if(now == http_date):
  #Push alert to chatbot!
  print('Modified!')
