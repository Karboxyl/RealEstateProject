import numpy as np
from bs4 import BeautifulSoup
import pandas as pd
import requests
from listing import lst 

def answer():
    while True:
        ans=input("Would you like to loop thourgh all postings Y/N ?")
        if ans.lower()=="y":
            return "https://www.nehnutelnosti.sk/vysledky?page=1"
                #https://www.nehnutelnosti.sk/vysledky/bernolakovo?page=2
                
        else:
            location=input("Please insert location name (Location must match the location in Nehnutelnosti)")
            return f"https://www.nehnutelnosti.sk/vysledky/{location}?page=1"
        
def find_last_page(url:str):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    page=soup.find("ul",attrs="MuiPagination-ul mui-nhb8h9")
    page_list=page.find_all("li")
    return int(page_list[-1].text.strip())

def load_listings(url:str,last_page:int):
    list_dictionary={}
    for page in range(1,last_page+1):
        #request url
        response=requests.get(f"{url}{page}")
        #parse response
        parsed_response=BeautifulSoup(response.text,'html.parser')
        #identify block with listings
        listings=parsed_response.find_all("div", class_="MuiStack-root mui-1xoye06")
        #loop thourgh listings and export data and create lst object
        for listing in listings:
            listing_name = listing.find("h2").text.strip()
            location = listing.find("p", attrs={"class": "MuiTypography-root MuiTypography-body2 MuiTypography-noWrap mui-3vjwr4"}).text.strip()
            price=listing.find("p",attrs={"class": "MuiTypography-root MuiTypography-h5 mui-7e5awq"}).text.strip()
            #check if price is available if not add -1
            if price=="Info v RK" or price=="Cena dohodou":
                price=-1
            elif "mes" in price:
                price=price.replace(" €/mes.","")
                print(price)
            else:
                price=price.replace("\xa0","")
                price=price[:len(price)-2]
                print(float(price))


            price_per_m=listing.find("p",attrs={"class": "MuiTypography-root MuiTypography-label1 mui-u7akpj"})
            if price_per_m is None:
                price_per_m=-1
            elif "mes" in listing.find("p",attrs={"class": "MuiTypography-root MuiTypography-label1 mui-u7akpj"}).text.strip():
                price_per_m=listing.find("p",attrs={"class": "MuiTypography-root MuiTypography-label1 mui-u7akpj"}).text.strip().replace(" €/m²/mes.","").replace(",","").replace(" ","")
                print (price_per_m)
            else:
                price_per_m=listing.find("p",attrs={"class": "MuiTypography-root MuiTypography-label1 mui-u7akpj"}).text.strip()
                price_per_m=price_per_m.replace(" €/m²","").replace(" ","").replace(",",".")
                print(price_per_m)
            new_listing=lst(listing_name,location,price,price_per_m)
            #list_dictionary[new_listing.name]={"listing_name":new_listing.name,"listing_location":new_listing.location,"listing_price":new_listing.price}

    print(list_dictionary)


#----------------------------Main------------------------------------------------------

def main():
    #Create dictionary for listings
    list_dictionary={}

    #Ask user if he wants to loop through all postings or let him choose the location
    url=answer()

    #find last page from li element
    last_page=find_last_page(url)

    #delete the url page number:
    url=url[:len(url)-1]

    #use the url and last page info to loop through all pages and all listings and return dictionary with these listings.
    list_dictionary=load_listings(url,last_page)
    #loop from first to last page and request url
    
    

main()


