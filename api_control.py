#-*-coding: utf-8-*-
import requests
import json
import matplotlib.pyplot as plt
import os
import datetime
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
       day = Currency.date()
       #if iso code is in list currency_list
       for i in currency_list:
            if i.iso == iso_code.upper():
                return i
       response = requests.get("http://api.nbp.pl/api/exchangerates/rates/c/"+iso_code+"/"+today+"/")
       if response.status_code == 200:
          parsed = json.loads(response.text)
          new_currency = Currency(response.status_code, parsed["code"], parsed["currency"], round(float(parsed["rates"][0]["ask"]), 2), round(float(parsed["rates"][0]["bid"]),2))
          currency_list.append(new_currency)
       else:
          new_currency = Currency(response.status_code, None, None, None, None)
       return new_currency

    def get_all_currencies():
        response = requests.get("http://api.nbp.pl/api/exchangerates/tables/c/")
        parsed = json.loads(response.text)
        for i in parsed[0]["rates"]:
            new_currency = Currency(response.status_code, i["code"], i["currency"], round(float(i["ask"]),2), round(float(i["bid"]),2))
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
            result = round(float(d_amount / output_price), 2)
        elif d_input != 'PLN' and d_output == 'PLN':
            result = round(float(d_amount * input_price), 2)
        elif d_input != 'PLN' and d_output != 'PLN' and d_input != d_output:
            result = round(float((input_price * d_amount) / output_price), 2)
        else:
            result = round(d_amount, 2)
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
        plt.xlabel("Days")
        plt.title("Chart for "+iso_code.upper())
        #mark start and end date
        plt.xticks([0, len(currency_values)-1], [start_date, end_date])

        # save chart to file
        project_path = os.getcwd()
        if not os.path.exists(project_path+"/charts"):
            os.mkdir(project_path+"/charts")
        plt.savefig(project_path+"/charts/"+iso_code+".png")
        currency_values.clear()
        #check if chart exists
        if os.path.isfile(project_path+"/charts/"+iso_code+".png"):
            return project_path+"/charts/"+iso_code+".png"
        else:
            return None

    def date():
        date = datetime.date.today()
        if date.weekday() == 6:
            date = date - datetime.timedelta(days=2)
        elif date.weekday() == 5:
            date = date - datetime.timedelta(days=1)
        return date.strftime("%Y-%m-%d")

