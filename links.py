import requests
import tkhtmlview
import tkinter
import bs4
from tkinter import*
import tkinter as tk
import functools
from bs4 import BeautifulSoup
url='https:www.bplans.com/'
website=requests.get(url)
website_text=website.text


soup =BeautifulSoup(website_txt)


for link in soup.find_all('a'):
# <a link in soup.find_all('a):
    link.append() 

