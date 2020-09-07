from bs4 import BeautifulSoup
import requests, sys
import time
from array import *
#https://www.olx.ro/imobiliare/alba-iulia/q-imobiliare/?search%5Bfilter_float_price%3Afrom%5D=20&search%5Bfilter_float_price%3Ato%5D=20000
inList=False
def sites(txt):
    site_list = ['olx', 'emag']
    url_list = ['https://www.olx.ro/']
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
            price_lower = "search%5Bfilter_float_price%3Afrom%5D="
            price_lower=price_lower+input("Lower price: ")
            price_higher = "&search%5Bfilter_float_price%3Ato%5D="
            price_higher=price_higher+input("Higher price: ")
            print(price_lower)
        else:
            price_lower="search%5Bfilter_float_price%3Afrom%5D=0"
            price_higher = "&search%5Bfilter_float_price%3Ato%5D=1000000000"
        #HOMES
        if search.lower() == "homes":
            place=input("What city?")
            query_list=["imobiliare",place,"casa",price_lower,price_higher]
            other_optionsTrue=input("Want other options? *not in query* eg. Rooms, balcony...   yes/no ")
            if other_optionsTrue == "yes":
                print("what should those be: (Ctrl+C when done)")
                other_options=[]
                try:
                    while True:
                        options=input()
                        other_options.append(options)
                except KeyboardInterrupt:
                    pass
            #Search on more sites with threading
            
            print("Starting searching...")
            count = 1
            url=url_list[0]+query_list[0]+"/"+query_list[1]+"/q-"+query_list[2]+"/?"+query_list[3]+query_list[4]
            #url = "http://www.olx.ro/imobiliare/alba-iulia/q-casa/?search%5Bfilter_float_price%3Afrom%5D=10+&amp;search%5Bfilter_float_price%3Ato%5D=100000"
            #url="https://www.olx.ro/oferta/1-2-duplex-de-lux-modern-str-lalelelor-cetate-langa-lidl-IDd68eu.html#bd464d27c7;promoted"
            headers = {'User-Agent': 'Mozilla/5.0'}
            print(url)
            r = requests.get(url,headers=headers, verify=False)

            soup=BeautifulSoup(r.text,'html.parser')
            soup.get_text()
           # soup.prettify()
            print(r.text)
                
