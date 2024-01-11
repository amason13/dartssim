import boto3
import json
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import time
import csv
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

PROJECT_PATH = os.getcwd()
PROJECT_PATH = PROJECT_PATH.replace("\\",'/')

def write_csv(name, mydict,field_names):
    file_exists = os.path.isfile(name+".csv")
    with open(name+'.csv', 'a', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        if not file_exists:
            writer.writeheader()
        writer.writerow(mydict)   


def read_list():
    with open('input.txt', 'r') as f:
        return f.readlines()


class WebDriver(object):

    def __init__(self):
        self.options = Options()

        self.options.binary_location = '/opt/headless-chromium'
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')

    def get(self):
        driver = Chrome('/opt/chromedriver', options=self.options)
        return driver


def lambda_handler(event, context):

    instance_ = WebDriver()
    browser = instance_.get()

    # ##### new code
    # chromeOptions = webdriver.ChromeOptions()
    # prefs = {"profile.managed_default_content_settings.images":2}
    # # chromeOptions.add_argument("--headless")
    # chromeOptions.add_experimental_option("prefs",prefs)
    # browser = webdriver.Chrome(chrome_options=chromeOptions,executable_path=PROJECT_PATH+'/chromedriver')
    # # PROXY = "194.28.8.141:49681" # IP:PORT or HOST:PORT

    # chromeOptions.add_argument('--proxy-server=%s' % PROXY)


    # browser = webdriver.Chrome(chrome_options=chromeOptions)
    # browser = webdriver.Chrome()
    browser.set_window_position(400, 40)
    browser.set_window_size(1300, 1024)
    wait = ui.WebDriverWait(browser,60)
    browser.get('https://live.dartsdata.com/')
    wait.until(lambda browser: browser.find_element_by_css_selector('iframe#iframeID'))
    src=browser.find_element_by_css_selector('iframe#iframeID').get_attribute("src")
    browser.get(src)
    wait.until(lambda browser: browser.find_element_by_css_selector('body > div.srl-wrapper > div > div.srl-content > div.srl-sidebar.srl-flex > div.srl-matchlist.srl-flex-child.sr-widget.sr-widget-level-0.sr-widgets-matchlist.sr-matchlist-common.sr-small > div > div.sr-matchlist-container.sr-has-calendar > div > div.sr-nano-scroller-content > div'))
    el = browser.find_element_by_css_selector('body > div.srl-wrapper > div > div.srl-content > div.srl-sidebar.srl-flex > div.srl-matchlist.srl-flex-child.sr-widget.sr-widget-level-0.sr-widgets-matchlist.sr-matchlist-common.sr-small > div > div.sr-matchlist-container.sr-has-calendar > div > div.sr-nano-scroller-content > div')
    browser.execute_script("arguments[0].click();", el)
    el.click()
    wait.until(lambda browser: browser.find_element_by_css_selector('div.sr-match-list > div.sr-match-container'))
    soup = BeautifulSoup(browser.page_source, "html.parser")
    match_list = soup.select('div.sr-match-list > div.sr-match-container')
    i=0
    while i < len(match_list):
        data_array=[]
        matchId = match_list[i].get('data-sr-matchid')
        browser.get(src + '#matchId=' + matchId)
        time.sleep(3)
        wait.until(lambda browser: browser.find_element_by_css_selector('table.sr-table > tbody > tr.sr-comment-item'))
        soup = BeautifulSoup(browser.page_source, "html.parser")
        # sr-team-name-away
        p1 = soup.select_one('div.sr-team-name-home').text.strip()
        p2 = soup.select_one('div.sr-team-name-away').text.strip()
        event = soup.select_one('div.sr-head-title-tournament-label').text.strip()
        date = soup.select_one('div.sr-footer-text').text.strip()
        set_ = 1
        leg = 1

        trs = soup.select('table.sr-table > tbody > tr.sr-comment-item')
        trs = trs[::-1]
        j=0
        while j < len(trs):
            tds = trs[j].select('td')
            try:
                first_td = tds[0].select_one('p.sr-txt').text.strip()
            except:
                j+=1
                continue
            last_td = tds[4].select_one('p.sr-txt').text.strip()
            if 'Will throw first' in first_td:
                throw = 1
                j+=1
                continue
            elif 'Will throw first' in last_td:
                throw = 2
                j+=1
                continue

            # text = first_td.replace(')').split('(')[1]
            d1 = ''
            d2 = ''
            d3 = ''
            try:
                text = first_td.replace(')','').split('points (')[1]
                throw = 1
                d1 = text.split(',')[0].strip()
                d2 = text.split(',')[1].strip()
                d3 = text.split(',')[2].strip()
            except:
                pass
            try:
                text = last_td.replace(')','').split('points (')[1]
                throw = 2
                d1 = text.split(',')[0].strip()
                d2 = text.split(',')[1].strip()
                d3 = text.split(',')[2].strip()
            except:
                pass
            if d1 == '':
                j+=1
                continue

            # date  event   p1  p2  set leg throw   d1  d2  d3

            data = {
                'date': date,
                'event': event,
                'p1': p1,
                'p2': p2,
                'set': set_,
                'leg': leg,
                'throw': throw,
                'd1': d1,
                'd2': d2,
                'd3': d3,
                }
            data_array.append(data)
        #     names=[]
        #     for key in data.keys():
        #         names.append(key)
        #     write_csv('data', data, names)
        # #     if old_list == len(reviews):
        # #         b+=1
        # #     else:
        # #         b=0
        # #     if b == 5:
        # #         break
        # #     print(len(reviews_ids))

            if 'Leg won' in first_td or 'Leg won' in last_td:
                leg+=1
                # j+=1
                # continue
            if 'Set won' in first_td or 'Set won' in last_td:
                set_+=1
                # j+=1
                # continue
            
            j+=1
        return data_array
        i+=1
    browser.quit()
