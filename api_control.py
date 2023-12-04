#-*-coding: utf-8-*-
import requests
import json
import matplotlib.pyplot as plt
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

    def convert_currencies(d_input, d_output, d_amount, choice): #choice == 1 - sell price, choice == 2 - buy price
        if d_input != 'PLN' or d_output != 'PLN':
            for i in currency_list:
                if i.iso == d_input:
                    if choice == 0: input_price = i.sell
                    else: input_price = i.buy
                if i.iso == d_output:
                    if choice == 0: output_price = i.sell
                    else: output_price = i.buy
        if d_input == 'PLN' and d_output != 'PLN':
            result = float(d_amount / output_price)
        elif d_input != 'PLN' and d_output == 'PLN':
            result = float(d_amount * input_price)
        elif d_input != 'PLN' and d_output != 'PLN' and d_input != d_output:
            result = float((input_price * d_amount) / output_price)
        else:
            result = d_amount
        return result

    def get_chart_data(iso_code, start_date, end_date):
        response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/"+iso_code+"/"+start_date+"/"+end_date+"/")
        parsed = json.loads(response.text)
        #add data to list
        currency_values = []
        for i in parsed["rates"]:
            currency_values.append(i["mid"])
            print(i["mid"])
        #draw chart
        plt.plot(currency_values)
        plt.ylabel("Price")
        #first day and last day
        plt.xlabel("Days")
        #select x axis ticks as first and last day
        plt.title("Chart for "+iso_code.upper())
        plt.show()
