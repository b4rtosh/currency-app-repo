#-*-coding: utf-8-*-
import requests
import json

def get_one_currency(iso_code):
   response = requests.get("http://api.nbp.pl/api/exchangerates/rates/c/"+iso_code+"/today/")
   if response.status_code == 200:
      parsed = json.loads(response.text)
      iso = parsed["code"]
      currency = parsed["currency"]
      sell = parsed["rates"][0]["ask"]
      buy = parsed["rates"][0]["bid"]
      answer = [response.status_code, iso, currency, sell, buy]
   else:
      answer = [response.status_code]
   return answer