import time
import selenium

import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

list_tweets=[]
list_names=[]
sentiment_result=[]
data={}

url='https://twitter.com/search?q=%23FuelShortageKE&src=trend_click&vertical=trends'
driver=webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(10)
def move_down():
    element=driver.find_element_by_tag_name('body')
     
        #tweets=driver.find_elements_by_xpath("//*[@class='css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0']")
    element.send_keys(Keys.PAGE_DOWN)
    driver.implicitly_wait(1)


def tweet_scrap():
    tweets=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@class='css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0']" )))
    print(tweets)

    
tweet_scrap()
move_down()




            
    
