from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

from urls import url


class scraper():

    def __init__(self,position,location):
        self.position = position
        self.location = location

    url = url()

    linkedin_url = url.indeed_url
    indeed_url = url.indeed_url
    naukri_url = url.naukri_url
    shine_url = url.shine_url

    def linkedin_data(self):

         
