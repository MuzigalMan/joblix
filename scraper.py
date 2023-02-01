from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
from bs4 import BeautifulSoup

from urls import url


class scraper():

    def __init__(self,position,location):
        self.position = position
        self.location = location
        self.url = url(position,location)

    driver = webdriver.Chrome(executable_path='./chromedriver.exe')

    def linkedin_data(self):

        self.driver.get(self.url.linkdin_url())


s = scraper('SDE', 'Hyderabad')
s.linkedin_data()
        