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
        num=site_list.index(txt.lower())
        print(site_list[num])
        print(url_list[num])
        f = open('links.txt', "w")
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
            old_url = url
            link_array = ['']
            try:
                while searching:
                    count=count+1
                    
                    url=old_url+"&page="+str(count)
                    print(requests.get(url, headers=headers))
                    print(url+ " Asta ii nou")
                    r=requests.get(url,headers=headers)
                    soup=BeautifulSoup(r.text,'html.parser')
                    soup.get_text()
                    soup.prettify()
                
                    for a in soup.find_all('a', href=True):
                        #print (a['href'])  
                        link_home=a['href']
                        timer1 = time.time()
                        if  ";promoted" not in link_home and link_home != "#" and link_home != " " and link_home != "javascript:void(0);" and "casa" in link_home or "page" in link_home:
                            home=requests.get(a['href'])
                            home_soup=BeautifulSoup(home.text,'html.parser')
                            home_soup.get_text()
                            descriere=home_soup.find("div", id="textContent")
                            if descriere != None:
                                descriere=home_soup.find("div",id="textContent").get_text()
                                if any(o in descriere for o in other_options):
                                    if(link_home not in link_array):
                                        link_array.append(link_home)
                                        print("Good")
                                        print(link_home)
                                        print(url)
                                        f.write(link_home)
                                        f.write("\n")
                                        timer2 = time.time()
                                        print(timer2-timer1)
                        if link_home == url +"&page=2":
                            break
            except KeyboardInterrupt:
                f.close()
                exit()
