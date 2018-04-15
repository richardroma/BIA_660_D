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

def scrape_all_reviews_on_page(review_total_element):
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

        # get top contributor text
        #review_contributor = 'top' in soup.find('a', attrs={'class': 'enthusiast-badge'}).text
        #data_dict['contributor'] = review_contributor

        review_data.append(data_dict)

    print(review_data)

    normal_delay = random.normalvariate(2, 0.5)
    print('Sleeping for {} seconds'.format(normal_delay))
    time.sleep(normal_delay)

    while True:
        try:
            next_page_bar = driver.find_element_by_id("""cm_cr-pagination_bar""")
            next_page = next_page_bar.find_element_by_class_name("a-last")
            next_page.click()
            normal_delay = random.normalvariate(2, 0.5)
            print('Sleeping for {} seconds'.format(normal_delay))
            time.sleep(normal_delay)

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

                # get top contributor text
                # review_contributor = 'top' in soup.find('a', attrs={'class': 'enthusiast-badge'}).text
                # data_dict['contributor'] = review_contributor

                review_data.append(data_dict)

        except:
            break

scrape_all_reviews_on_page(review_total_element)

print(review_data)