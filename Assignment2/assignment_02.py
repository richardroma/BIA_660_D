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

driver.get('http://www.mlb.com')

stats_header_bar = driver.find_element_by_class_name('megamenu-navbar-overflow__menu-item--stats')

stats_header_bar.click()

stats_line_items = stats_header_bar.find_elements_by_tag_name('li')

stats_line_items[2].click()

hitting_season_element = driver.find_element_by_id('st_hitting_season')
season_select = Select(hitting_season_element)
season_select.select_by_value('2015')

wait = WebDriverWait(driver, 10)

team_hr_stats = wait.until(EC.visibility_of_element_located((By.ID, 'datagrid')))

print('The HR dropdown in the header was loaded successfully. The mouse will move over the element after a short delay')
normal_delay = random.normalvariate(2, 0.5)
print('Sleeping for {} seconds'.format(normal_delay))
time.sleep(normal_delay)
print('Now moving mouse...')
ActionChains(driver).move_to_element(team_hr_stats).perform()

team_hr_total = team_hr_stats.find_elements_by_tag_name('th')

team_hr_total[10].click()

data_div_1 = driver.find_element_by_id('datagrid')
data_html_1 = data_div_1.get_attribute('innerHTML')

import bs4
import requests

soup_1 = bs4.BeautifulSoup(data_html_1, 'html5lib')


def extract_team_hr_data(data_element):
    data_html_1 = data_element.get_attribute('innerHTML')
    soup_1 = bs4.BeautifulSoup(data_html_1, 'html5lib')

    column_names = [t.text.replace('▼', ' ').replace('▲', ' ').strip() for t in soup_1.thead.tr.findAll('th')]

    row_lists = []
    for row in soup_1.tbody.findAll('tr'):
        row_lists.append([col.text for col in row.findAll('td')])

    df = pd.DataFrame(row_lists, columns=column_names)

    numeric_fields = ['HR']
    for field in numeric_fields:
        df[field] = pd.to_numeric(df[field])

    return df

df = extract_team_hr_data(data_div_1)
team_name = df.sort_values('HR', ascending=False).iloc[0]['Team']  # With highest HR

# Write team name string to file
with open('/Users/rickroma/Desktop/Assignment2/Question_1.csv', 'w') as f_output:
    f_output.write(team_name)

df_al = df[df.League == 'AL']['HR'].mean()
df_nl = df[df.League == 'NL']['HR'].mean()

if df_al > df_nl:
    print(df_al)
else:
    print(df_nl)







