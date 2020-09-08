from bs4 import BeautifulSoup
import requests, sys
import time
import threading 
from multiprocessing import Process
#from array import *
#https://www.olx.ro/imobiliare/alba-iulia/q-imobiliare/?search%5Bfilter_float_price%3Afrom%5D=20&search%5Bfilter_float_price%3Ato%5D=20000
inList=False
query_list=[]
url_list=[]
other_options=[]

def sites(txt):
    
    site_list = ['olx', 'emag']
    url_list.append('https://www.olx.ro/')
    url_list.append("https://www.storia.ro/")
    if txt.lower() in site_list:
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
        else:
            price_lower="search%5Bfilter_float_price%3Afrom%5D=0"
            price_higher = "&search%5Bfilter_float_price%3Ato%5D=1000000000"
        #HOMES
        if search.lower() == "homes":
            place=input("What city?")
            #query_list.append(["imobiliare",place,"casa",price_lower,price_higher])
            query_list.append("imobiliare")
            query_list.append(place)
            query_list.append("casa")
            query_list.append(price_lower)
            query_list.append(price_higher)
            #print(query_list)
            other_optionsTrue=input("Want other options? *not in query* eg. Rooms, balcony...   yes/no ")
            if other_optionsTrue == "yes":
                print("what should those be: (Ctrl+C when done)")
                
                try:
                    while True:
                        options=input()
                        other_options.append(options)
                except KeyboardInterrupt:
                    pass
            #Search on more sites with threading
            
            print("Starting searching...")
            #run_event=Thread.Event()
            
            #Thread(target=thread1_olx_home).start()
            #Thread(target=therad2_stroia_home).start()

            #t1.join()
            #t2.join()
            try:
                t1 = threading.Thread(target=thread1_olx_home)
                t2 = threading.Thread(target=therad2_stroia_home)
                t1.start()
                t2.start()

                while 1:
                    time.sleep(.01)
            except KeyboardInterrupt:
                t1.join()
                t1.join()
                exit()
                


def thread1_olx_home():
    count = 0
    #print(other_options)
    url = url_list[0]+query_list[0]+"/"+query_list[1] +"/q-"+query_list[2]+"/?"+query_list[3]+query_list[4]
    headers = {'User-Agent': 'Mozilla/5.0'}
    print(url)
    print(requests.get(url, headers=headers))
    searching = True
    old_url = url
    link_array = ['']
    try:
        while searching:
            
            count = count+1
            print(str(count) + " olx")
            url = old_url+"&page="+str(count)
            #print(requests.get(url, headers=headers))
            #print(url + " Asta ii nou")
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.text, 'html.parser')
            soup.get_text()
            soup.prettify()
            
            for a in soup.find_all('a', href=True):
                link_home = a['href']
               # print(link_home)
                #timer1 = time.time()
                if ";promoted" not in link_home and link_home != "#" and link_home != " " and link_home != "javascript:void(0);" and "casa" in link_home or "page" in link_home:
                   home = requests.get(a['href'])
                   home_soup = BeautifulSoup(home.text, 'html.parser')
                   home_soup.get_text()
                   descriere = home_soup.find("div", id="textContent")
                   if descriere != None:
                        descriere = home_soup.find("div", id="textContent").get_text()
                        if all(o in descriere for o in other_options):
                            if(link_home not in link_array):
                                link_array.append(link_home)
                                f=open('links.txt',"a")
                                print("Good")
                                #print(link_home)
                               # print(url)
                                f.write(link_home)
                                f.write("\n")
                                #timer2 = time.time()
                                #print(timer2-timer1)
                                f.close()
                                if link_home == url + "&page=":
                                    break
    except KeyboardInterrupt:
        f.close()
        exit()
        pass



def therad2_stroia_home():
    #https://www.storia.ro/vanzare/casa/alba/?search%5Bfilter_float_price%3Ato%5D=90000
    count_stroia = 0
    #print(other_options)
    url_stroia = url_list[1]+"/vanzare/casa/"+query_list[1]+"/?search"+query_list[4]
    headers = {'User-Agent': 'Mozilla/5.0'}
    print(url_stroia)
    print(requests.get(url_stroia, headers=headers))
    searching = True
    old_url_stroia = url_stroia
    link_array_stroia = ['']
    try:
        while searching:
            count_stroia = count_stroia+1
            print(str(count_stroia)+" stroia")
            url_stroia = old_url_stroia+"&page="+str(count_stroia)
            #print(requests.get(url_stroia, headers=headers))
            #print(url_stroia + " Asta ii nou")
            r_stroia = requests.get(url_stroia, headers=headers)
            soup_stroia = BeautifulSoup(r_stroia.text, 'html.parser')
            soup_stroia.get_text()
            soup_stroia.prettify()
            for a_stroia in soup_stroia.find_all('a', href=True):
                link_home_stroia = a_stroia['href']
                #timer1_stroia = time.time()
                if "javascript:void(0);" not in link_home_stroia and "&map=1" not in link_home_stroia and ";promoted" not in link_home_stroia and link_home_stroia != "#" and link_home_stroia != " " and link_home_stroia != "javascript:void(0)" and "casa" in link_home_stroia or "page" in link_home_stroia and "https://" in link_home_stroia:
                  # print("stroia" + link_home_stroia)
                   home_stroia = requests.get(a_stroia['href'])
                   home_soup_stroia = BeautifulSoup(home_stroia.text, 'html.parser')
                   home_soup_stroia.get_text()
                   descriere_stroia = home_soup_stroia.find("div", {"class":"css-uiakpw"})
                   if descriere_stroia != None:
                       descriere_stroia = home_soup_stroia.find(
                           "div", {"class": "css-uiakpw"}).get_text()
                       if all(o_stroia in descriere_stroia for o_stroia in other_options):
                           if(link_home_stroia not in link_array_stroia):
                               link_array_stroia.append(link_home_stroia)
                               stroia=open('stroia.txt',"a")
                               print("gasit")
                               #print(link_home_stroia)
                               #print(url_stroia)
                               stroia.write(link_home_stroia)
                               stroia.write("\n")
                               #timer2_stroia = time.time()
                               #print(timer2_stroia-timer1_stroia)
                               stroia.close()
                               if link_home_stroia == url_stroia + "&page=":
                                   break
    except KeyboardInterrupt:
        exit()
        pass


