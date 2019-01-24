import json
import os
import re
import requests
from time import strftime, localtime
from datetime import datetime, timedelta

from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Helpers():

    def wait_presence_by_id(self, driver, el, wait=10):
        return WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.ID, el)))

    def wait_presence_all_by_id(self, driver, el, wait=10):
        return WebDriverWait(driver, wait).until(EC.presence_of_all_elements_located((By.ID, el)))

    def wait_presence_all_by_class(self, driver, el, wait=10):
        return WebDriverWait(driver, wait).until(EC.presence_of_all_elements_located((By.CLASS_NAME, el)))

    def wait_presence_by_selector(self, driver, el, wait=10):
        return WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.CSS_SELECTOR, el)))

    def wait_presence_by_tag(self, driver, el, wait=10):
        return WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.TAG_NAME, el)))

    def wait_clickable_by_id(self, driver, el, wait=10):
        return WebDriverWait(driver, wait).until(EC.element_to_be_clickable((By.ID, el)))

    def wait_visibility_by_id(self, driver, el, wait=10):
        return WebDriverWait(driver, wait).until(EC.visibility_of_element_located((By.ID, el)))

    def wait_visibility_by_class(self, driver, el, wait=10):
        return WebDriverWait(driver, wait).until(EC.visibility_of_element_located((By.CLASS_NAME, el)))

    def wait_visibility_by_selector(self, driver, el, wait=10):
        return WebDriverWait(driver, wait).until(EC.visibility_of_element_located((By.CSS_SELECTOR, el)))

    def wait_presence_by_xpath(self, driver, el, wait=10):
        return WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.XPATH, el)))

    def wait_all_presence_by_xpath(self, driver, els, wait=10):
        return WebDriverWait(driver, wait).until(EC.presence_of_all_elements_located((By.XPATH, els)))

    def wait_visiblity_by_xpath(self, driver, el, wait=10):
        return WebDriverWait(driver, wait).until(EC.visibility_of_element_located((By.XPATH, el)))

    def wait_clickable_by_xpath(self, driver, el, wait=10):
        return WebDriverWait(driver, wait).until(EC.element_to_be_clickable((By.XPATH, el)))

    def wait_url_contains(self, driver, url, wait=10):
        return WebDriverWait(driver, wait).until(EC.url_contains(url))

    def switch_window(self, driver, link):
        print(driver.current_url)
        # current_window = driver.current_window_handle
        link.click()
        # this loop will open any new window
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
        print(driver.current_url)

    def press_enter(self, obj):
        return obj.send_keys(Keys.RETURN)

    def send_text(self, obj, txt):
        obj.clear()
        return obj.send_keys(txt)

    def alpha(self):
        alpha = {}
        for k,v in self.environment('ALPHA').items():
            alpha[k] = v
        return alpha

    def page_main(self, env):
        return self.environment('ALPHA')["URL_CHAT_API"]

    def get_page_main(self, driver):
        if self.environment('ALPHA')["URL_CHAT_API"] not in driver.current_url:
            driver.get(self.environment('ALPHA')["URL_CHAT_API"])

    def regex_findall(self, regex, phrase):
        return re.findall(regex, str(phrase))

    def environment(self, env):
        base = ''
        with open(self.path_web('data/environment.json'), 'r') as e:
            base_urls = json.load(e)
        with open(self.path_web('data/link.json'), 'r') as l:
            urls = json.load(l)

        for k, v in base_urls.items():
            if env == k:
                base = v

        for k, v in urls.items():
            urls[k] = base + v

        return urls

    def path_web(self, file):
        cwd = os.getcwd()
        # web = os.path.dirname(cwd)
        # return os.path.join(web, file)
        return os.path.join(os.path.dirname(cwd), file)

    def scroll_to_element(self, driver, el):
        ac = ActionChains(driver)
        return ac.move_to_element(el).click().perform()

    def check_element_exist(self, el):
        try:
            el
        except NoSuchElementException:
            return False
        return True

    def check_http_response_no_auth(self, el):
        return requests.get(el)

    def img_response_checker(self, url):
        r = requests.get(url)
        if r.status_code == 200 and r.headers['Content-Type'] == 'image/jpeg' and int(r.headers['Content-Length']) > 0:
            return 'image_ok'
        else:
            return 'image_error'

    def internet_time(self):
        try:
            import ntplib

            client = ntplib.NTPClient()
            response = client.request('pool.ntp.org')
            return strftime('%a, %d %b %H:%M:%S', localtime(response.tx_time))
        except:
            print('Could not sync with time server, use local time instead')
            return strftime('%a, %d %b %H:%M:%S', localtime())

    def time_delta_one_minute(self, t1, t2):
        tdelta = datetime.strptime(t2[12:], '%H:%M:%S') - datetime.strptime(t1[12:], '%H:%M:%S')
        if abs(timedelta.total_seconds(tdelta)) < 61:
            return True
        else:
            return False