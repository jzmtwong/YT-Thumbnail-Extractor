from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import os
import time


def init_browser():
    #adding local connection
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

#extract YT thumbnail from URL
def yt_extract(url):
    #import soup
    from bs4 import BeautifulSoup
    #create brower visit
    response = requests.get(url)
    #taking time to load, so need to sleep to refresh
    import time
    time.sleep(3)
    soup = BeautifulSoup(response.text, 'html.parser')
    # scape the Thumbnail Image link URL

    rough_link = soup.find('div', class_='watch-main-col').find('span',itemprop='thumbnail').link

    #extract url
    thumbnail_url = (rough_link['href'])

    # Close the browser after scraping
    browser.quit()

    # Return results
    return(thumbnail_url)
