import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.support.select import Select

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import random
import time

driver = webdriver.Chrome(executable_path='/Users/rickroma/Desktop/Assignment2/chromedriver')

import bs4
import requests

driver.get('https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM')
review_total_element = driver.find_element_by_id('cm_cr-review_list')
review_data = []
for review in review_total_element.find_elements_by_css_selector("div[class='a-section celwidget']"):
    soup = bs4.BeautifulSoup(review.get_attribute("innerHTML"),'html5lib')
    data_dict = {}

    # get headline
    headline_text = soup.div.find('a', attrs= {'class': 'review-title'}).text
    data_dict['headline'] = headline_text

    # get number of stars
    review_stars = soup.find('a').text
    # do something here to get only the number of stars from text like "3.0 out of 5 stars"
    data_dict['stars'] = review_stars

    # get review date
    review_date = soup.find('span', attrs= {'class': 'review-date'}).text[3:]
    data_dict['date'] = review_date

    # get reviewer name
    review_name = soup.find('a', attrs= {'class': 'author'}).text
    data_dict['name'] = review_name

    # get verified purchase status
    review_status = soup.find('span', attrs= {'class': 'a-size-mini a-color-state a-text-bold'}).text
    data_dict['status'] = review_status

    # get review text
    review_text = soup.find('span', attrs= {'class': 'a-size-base review-text'}).text
    data_dict['text'] = review_text

    # get number of people who find review helpful
    review_helpful = soup.find('span', attrs = {'class': 'review-votes'}).text
    data_dict['helpful'] = review_helpful

    # get top contributor text

    review_data.append(data_dict)

    review_data = []

while (there_is_a_next_page_of_reviews()):
    go_next_page_of_reviews()

    for review in review_total_element.find_elements_by_css_selector("div[class='a-section celwidget']"):
        soup = bs4.BeautifulSoup(review.get_attribute("innerHTML"), 'html5lib')
        data_dict = {}

        # get headline
        headline_text = soup.div.find('a', attrs={'class': 'review-title'}).text
        data_dict['headline'] = headline_text

        # get number of stars
        review_stars = soup.find('a').text
        # do something here to get only the number of stars from text like "3.0 out of 5 stars"
        data_dict['stars'] = review_stars

        # get review date
        review_date = soup.find('span', attrs={'class': 'review-date'}).text[3:]
        data_dict['date'] = review_date

        # get reviewer name
        review_name = soup.find('a', attrs={'class': 'author'}).text
        data_dict['name'] = review_name

        # get verified purchase status
        review_status = soup.find('span', attrs={'class': 'a-size-mini a-color-state a-text-bold'}).text
        data_dict['status'] = review_status

        # get review text
        review_text = soup.find('span', attrs={'class': 'a-size-base review-text'}).text
        data_dict['text'] = review_text

        # get number of people who find review helpful
        review_helpful = soup.find('span', attrs={'class': 'review-votes'}).text
        data_dict['helpful'] = review_helpful

print(review_data)
