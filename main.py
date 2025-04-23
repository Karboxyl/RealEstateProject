import numpy as np
from bs4 import BeautifulSoup
import pandas as pd
import requests
import json


def main():
    url="https://www.nehnutelnosti.sk/vysledky/bernolakovo?page=2"
    response=requests.get(url)
    print(response)

    soup=BeautifulSoup(response.text,'html.parser')
    post_name = soup.find_all("h2", attrs={"data-test-id": "text"})
    post_price=soup.find_all(attrs={"class":"MuiTypography-root MuiTypography-h5 mui-7e5awq","data-test-id": "text"})
    post_location=soup.find_all("p",attrs={"class":"MuiTypography-root MuiTypography-body3 MuiTypography-noWrap mui-e9ka76","data-test-id": "text"})




    for posting in post_location:
        print(posting)
        print(posting.text.strip())

main()
