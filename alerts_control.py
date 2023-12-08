#-*-coding: utf-8-*-
from api_control import currency_list
import os
import requests
import json
import datetime

def get_alerts():
    currency_alerts = []
    project_path = os.getcwd()
    global currency_list
    if not os.path.exists(project_path +"/alerts.txt"):
        return None
    else:
        with open(project_path +"/alerts.txt", "r") as file:
            for line in file:
                iso = line.split(';')[0]
                alert = line.split(';')[1]
                for i in currency_list:
                    if i.iso == iso:
                        price = i.buy
                        if float(price) >= float(alert):
                            status = "Above"
                        else:
                            status = "Below"
                        currency_alerts.append((iso, alert, price, status))
                        break
        return currency_alerts


def make_alerts():
    alerts = get_alerts()
    messages = []
    if alerts == None:
        return None
    else:
        for i in alerts:
            if i[3] == "Below":
                messages.append((i[0], i[2]))
    return messages

