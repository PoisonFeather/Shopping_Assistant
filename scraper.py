from bs4 import BeautifulSoup
import requests, sys
import time
from array import *
#https://www.olx.ro/imobiliare/alba-iulia/q-imobiliare/?search%5Bfilter_float_price%3Afrom%5D=20&search%5Bfilter_float_price%3Ato%5D=20000
inList=False
def sites(txt):
    site_list = ['olx', 'emag']
    url_list = ['https://www.olx.ro/oferte/q-']
    if txt.lower() in site_list:
        print("ok...")
        num=site_list.index(txt.lower())
        print(site_list[num])
        print(url_list[num])

        print("What do you want to search for?")
        print("Homes:")
        print("Apartments:")
        print("Shoes")
        print("Tv's:")
        print("Other query:  (0)")
        search=input(": ")
        print("Do you have a price range? *€*")
        price_true=input("yes/no ")
        if price_true.lower() == "yes":
            price_lower=input("Lower price: ")
            price_higher=input("Higher price: ")
        else :
            price_lower=0
            price_higher= 100000000000
        #HOMES
        if search.lower() == "homes":
            place=input("What city?")
             




    else:
        print("ERROR 1")
        print("Not in list")
    
