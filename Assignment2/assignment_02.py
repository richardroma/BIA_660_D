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

#Question 1

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

print(df.iat[0,1])

# Write team name string to file
df.to_csv('/Users/rickroma/Desktop/Assignment2/Question_1a.csv')

# Write team name string to file
with open('/Users/rickroma/Desktop/Assignment2/Question_1b.csv', 'w') as f_output:
    f_output.write(team_name)

#Question 2

df.to_csv('/Users/rickroma/Desktop/Assignment2/Question_2a.csv')

df_al = df[df.League == 'AL']['HR'].mean()
df_nl = df[df.League == 'NL']['HR'].mean()

if df_al > df_nl:
    print("AL", df_al)
else:
    print("NL", df_nl)

#Question 2b

inning_stats = driver.find_element_by_id('st_hitting_hitting_splits')
inning_select = Select(inning_stats)
inning_select.select_by_value('i01')

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

data_div_2 = driver.find_element_by_id('datagrid')
data_html_2 = data_div_2.get_attribute('innerHTML')

soup_2 = bs4.BeautifulSoup(data_html_2, 'html5lib')

def extract_first_inn_hr_data(data_element):
    data_html_2 = data_element.get_attribute('innerHTML')
    soup_2 = bs4.BeautifulSoup(data_html_2, 'html5lib')

    column_names = [t.text.replace('▼', ' ').replace('▲', ' ').strip() for t in soup_2.thead.tr.findAll('th')]

    row_lists = []
    for row in soup_2.tbody.findAll('tr'):
        row_lists.append([col.text for col in row.findAll('td')])

    df = pd.DataFrame(row_lists, columns=column_names)

    numeric_fields = ['HR']
    for field in numeric_fields:
        df[field] = pd.to_numeric(df[field])

    return df

df2 = extract_first_inn_hr_data(data_div_2)

df2.to_csv('/Users/rickroma/Desktop/Assignment2/Question_2b.csv')

print(df2.iat[0,1])

#Question 3

driver.get('http://www.mlb.com')

stats_header_bar = driver.find_element_by_class_name('megamenu-navbar-overflow__menu-item--stats')

stats_header_bar.click()

stats_line_items = stats_header_bar.find_elements_by_tag_name('li')

stats_line_items[0].click()

player_season_element = driver.find_element_by_id('sp_hitting_season')
player_select = Select(player_season_element)
player_select.select_by_value('2017')

season_type_element = driver.find_element_by_id('sp_hitting_game_type')
season_type_select = Select(season_type_element)
season_type_select.select_by_value("'R'")

yank_element = driver.find_element_by_id('sp_hitting_team_id')
yank_type_select = Select(yank_element)
yank_type_select.select_by_value("147")

data_div_3 = driver.find_element_by_id('datagrid')
data_html_3 = data_div_3.get_attribute('innerHTML')

def extract_player_hitting_data(data_element):
    data_html_3 = data_element.get_attribute('innerHTML')
    soup_3 = bs4.BeautifulSoup(data_html_3, 'html5lib')

    column_names = [t.text.replace('▼', ' ').replace('▲', ' ').strip() for t in soup_3.thead.tr.findAll('th')]

    row_lists = []
    for row in soup_3.tbody.findAll('tr'):
        row_lists.append([col.text for col in row.findAll('td')])

    df = pd.DataFrame(row_lists, columns=column_names)

    numeric_fields = ['HR']
    for field in numeric_fields:
        df[field] = pd.to_numeric(df[field])

    return df

df3 = extract_player_hitting_data(data_div_3)

df3.to_csv('/Users/rickroma/Desktop/Assignment2/Question_3.csv')

#filtered_df3 = df3.sort_values[(df3['AVG']) & (df3['AB'] >= '30')]
#print(filtered_df3)


#Question 4

driver.get('http://www.mlb.com')

stats_header_bar = driver.find_element_by_class_name('megamenu-navbar-overflow__menu-item--stats')

stats_header_bar.click()

stats_line_items = stats_header_bar.find_elements_by_tag_name('li')

stats_line_items[0].click()

hitting_average_element = driver.find_element_by_id('sp_hitting_season')
hitting_average_select = Select(hitting_average_element)
hitting_average_select.select_by_value('2015')

season_type_element = driver.find_element_by_id('sp_hitting_game_type')
season_type_select = Select(season_type_element)
season_type_select.select_by_value("""'R'""")

wait = WebDriverWait(driver, 10)

team_ab_stats = wait.until(EC.visibility_of_element_located((By.ID, 'datagrid')))

print('The AB dropdown in the header was loaded successfully. The mouse will move over the element after a short delay')
normal_delay = random.normalvariate(2, 0.5)
print('Sleeping for {} seconds'.format(normal_delay))
time.sleep(normal_delay)
print('Now moving mouse...')
ActionChains(driver).move_to_element(team_ab_stats).perform()

team_ab_total = team_ab_stats.find_elements_by_tag_name('th')

team_ab_total[7].click()

data_div_4 = driver.find_element_by_id('datagrid')
data_html_4 = data_div_4.get_attribute('innerHTML')

def extract_player_ab_data(data_element):
    data_html_4 = data_element.get_attribute('innerHTML')
    soup_4 = bs4.BeautifulSoup(data_html_4, 'html5lib')

    column_names = [t.text.replace('▼', ' ').replace('▲', ' ').strip() for t in soup_4.thead.tr.findAll('th')]

    row_lists = []
    for row in soup_4.tbody.findAll('tr'):
        row_lists.append([col.text for col in row.findAll('td')])

    df = pd.DataFrame(row_lists, columns=column_names)

    numeric_fields = ['HR']
    for field in numeric_fields:
        df[field] = pd.to_numeric(df[field])

    return df

df4 = extract_player_ab_data(data_div_4)

df4.to_csv('/Users/rickroma/Desktop/Assignment2/Question_4.csv')

#print(df4.loc[1:'Player', 'Team', 'Pos'])

#Question 5




