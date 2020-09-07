from bs4 import BeautifulSoup
import requests, sys
import time
#from array import *
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
        f = open("Shopping_Assistant\links.txt", "w")
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
        casefaine=[]
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
            count = 0
            url=url_list[0]+query_list[0]+"/"+query_list[1]+"/q-"+query_list[2]+"/?"+query_list[3]+query_list[4]
            #url = "http://www.olx.ro/imobiliare/alba-iulia/q-casa/?search%5Bfilter_float_price%3Afrom%5D=10+&amp;search%5Bfilter_float_price%3Ato%5D=100000"
            #url="https://www.olx.ro/oferta/1-2-duplex-de-lux-modern-str-lalelelor-cetate-langa-lidl-IDd68eu.html#bd464d27c7;promoted"
            headers = {'User-Agent': 'Mozilla/5.0'}
            print(url)
            print(requests.get(url,headers=headers))
           # r=requests.get(url,headers=headers)

           # soup=BeautifulSoup(r.text,'html.parser')
            #soup.get_text()
           # soup.prettify()
            searching=True
            #    print(soup.find_all('a',href=True))
            while searching:
                count=count+1
                print("BAAAAAAAAAAAAAAAAAAAAAAA")
                url=url+"&page="+str(count)
                print(url)
                print("BAAAAAAAAAAAAAA")
                r=requests.get(url,headers=headers)
                soup=BeautifulSoup(r.text,'html.parser')
                soup.get_text()
                soup.prettify()
                for a in soup.find_all('a', href=True):
                    #print (a['href'])  
                    link_home=a['href']
                    if  link_home != "#" and link_home != " " and link_home != "javascript:void(0);" and "casa" in link_home or "page" in link_home:
                        print(link_home)
                        home=requests.get(a['href'])
                        home_soup=BeautifulSoup(home.text,'html.parser')
                        home_soup.get_text()
                        #print(home_soup.find_all('p'))
                        #other_options[]
                        descriere=home_soup.find("div", id="textContent")
                        #print(descriere)
                        if descriere != None:
                            descriere=home_soup.find("div",id="textContent").get_text()
                            #print(options)
                            if any(o in descriere for o in other_options):
                                print("Good")
                                #casefaine.append(link_home)
                                print(link_home)
                                f.write(link_home)
                                f.write("\n")
                    if link_home == url +"&page=2":
                        print(casefaine)
                        break
                        #print(link_home)
                    #else:
                        #print("")
