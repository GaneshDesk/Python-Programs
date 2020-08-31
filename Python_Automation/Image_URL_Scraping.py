"""Automation script which fetch URL of all images using Beautiful Soup."""

import os
import bs4
import requests
from sys import *
from urllib.request import urlopen

def ImageScrapper(url):

    conection = urlopen(url)

    raw_html = conection.read()

    conection.close()

    page_soup=bs4.BeautifulSoup(raw_html,"html.parser")

    container = page_soup.findAll("div",{"class":"item-container"})

    return container

def main():
    print("Image Scrapper Application .")

    print("Aplication name : "+argv[0])

    if(len(argv) == 2):
        if(argv[1]=='-h')or(argv[1]=='-H'):
            print("this Script is used to fetch URL of Images.")
            exit()

        if(argv[1]=='-u')or(argv[1]=='-U'):
            print("Usage : ApplicationName")
            exit()    

    try:
        url =""

        listout = ImageScrapper(url)

        print("URLs of Images")
        for elements in listout:
            print(elements.a.img['data-src'])

    except Exception as E:
        print("Error : Invalid Input.",E)       

if __name__=='__main__':
    main()        