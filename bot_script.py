import time
import random

import smtplib, ssl
from email.message import EmailMessage

from selenium import webdriver as wd
# from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "aboniet99@gmail.com"  # Enter your address
receiver_email = "aboniet99@gmail.com"  # Enter receiver address
password = 'edpcyhwabfrxzoqq'

def send_email(price):
    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = receiver_email
    em['Subject'] = price
    em.set_content('https://tix.axs.com/hlocGwAAAADKRn%2bjAQAAAABm%2fv%2f%2f%2fwD%2f%2f%2f%2f%2fC0ZvcmVzdEhpbGxzAP%2f%2f%2f%2f%2f%2f%2f%2f%2f%2f/shop/search?skin=foresthills&tags=&cpch=&cpdate=&cpcn=&cpsrc=&intoff=&cid=&utm_source=&utm_medium=&utm_campaign=&utm_term=&utm_content=&aff=&clickref=&q=e25e5f32-bcf4-459a-bdf0-b068a98659e1&p=658943a9-9f93-4dcb-99b0-bf9bca909dc3&ts=1687936608&c=axs&e=45484301427492166&rt=Safetynet&h=17b216d42ebbf611a531efeb3f2852b2')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, em.as_string())

def parse_price_string(price_string):
    # Remove the dollar sign and decimal part from the string
    price_string = price_string.replace('$', '')
    price_string = price_string.split('.')[0]  # Keep only the whole number part

    # Convert the remaining string to an integer
    price_int = int(price_string)

    return price_int


options = wd.ChromeOptions()
options.add_experimental_option("detach", True)
browser = wd.Chrome(options=options)
browser.get('https://tix.axs.com/hlocGwAAAADKRn%2bjAQAAAABm%2fv%2f%2f%2fwD%2f%2f%2f%2f%2fC0ZvcmVzdEhpbGxzAP%2f%2f%2f%2f%2f%2f%2f%2f%2f%2f/shop/search?skin=foresthills&tags=&cpch=&cpdate=&cpcn=&cpsrc=&intoff=&cid=&utm_source=&utm_medium=&utm_campaign=&utm_term=&utm_content=&aff=&clickref=&q=e25e5f32-bcf4-459a-bdf0-b068a98659e1&p=658943a9-9f93-4dcb-99b0-bf9bca909dc3&ts=1687936608&c=axs&e=45484301427492166&rt=Safetynet&h=17b216d42ebbf611a531efeb3f2852b2')

time.sleep(30)
accept_cookies_button = browser.find_element(By.ID, 'onetrust-accept-btn-handler')
accept_cookies_button.click()

# click the body
# general_click = browser.find_element(By.XPATH,'/html/body')
# general_click.click()

time.sleep(30)
ga_bowl_button = browser.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div[3]/div/div[2]/div')
action = ActionChains(browser)
action.double_click(on_element = ga_bowl_button)
action.perform()

time.sleep(10)
price_text = browser.find_element(By.XPATH, '//*[@id="GA_SELECTOR"]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/span/span/span')
print(price_text.text)

price_int = parse_price_string(price_text.text)

# if price_int < 250:
send_email(price_text.text)

plus_button = browser.find_element(By.XPATH, '//*[@id="GA_SELECTOR"]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/button[2]')
plus_button.click()

time.sleep(random.randint(3, 7))

continue_button = browser.find_element(By.CLASS_NAME, 'ga-selector-continue')
continue_button.click()

time.sleep(random.randint(2, 6))

checkout_button = browser.find_element(By.CLASS_NAME, 'pre-cart-summary__label')
checkout_button.click()

time.sleep(random.randint(5, 10))

axn_mobile_id = browser.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div')
axn_mobile_id.click()

time.sleep(random.randint(3, 7))

order_summary_button = browser.find_element(By.ID, 'order-summary__next__btn--delivery')
order_summary_button.click()
    