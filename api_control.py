#-*-coding: utf-8-*-
import requests
import json

global currency_list
currency_list = []

class Currency:
    def __init__(self, status, iso, name, sell, buy):
        self.status = status
        self.iso = iso
        self.name = name
        self.sell = sell
        self.buy = buy


    def get_one_currency(iso_code):
       #if iso code is in list currency_list
       for i in currency_list:
            if i.iso == iso_code.upper():
                return i
       response = requests.get("http://api.nbp.pl/api/exchangerates/rates/c/"+iso_code+"/2023-12-01/")
       if response.status_code == 200:
          parsed = json.loads(response.text)
          new_currency = Currency(response.status_code, parsed["code"], parsed["currency"], parsed["rates"][0]["ask"], parsed["rates"][0]["bid"])
          currency_list.append(new_currency)
       else:
          new_currency = Currency(response.status_code, None, None, None, None)
       return new_currency

    def get_all_currencies():
        response = requests.get("http://api.nbp.pl/api/exchangerates/tables/c/")
        parsed = json.loads(response.text)
        for i in parsed[0]["rates"]:
            new_currency = Currency(response.status_code, i["code"], i["currency"], i["ask"], i["bid"])
            currency_list.append(new_currency)