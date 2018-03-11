import os
import sys
from time import sleep
import requests
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller
import random
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

os.environ["MOZ_HEADLESS"]="1"
binary = FirefoxBinary("/usr/lib/firefox/firefox", log_file=sys.stdout)
driver = webdriver.Firefox(firefox_binary=binary)

"""
I found that having the loop run on its own without any sleep() or pauses led to the same ip address over and over again
But, as I was manually typing it out in the terminal (via >>>), it actually changed IPs
If you want to, you can se the sleep statements to be quicker but you are more likely to run into the wall with the same IP
"""

ip_list = []
user_list = []
cur_ip = None
ua = UserAgent()
keyboard_chars = "qwertyuiopasdfghjklzxcvbnm0123456789"

def firefox():
	driver.get("https://news.ycombinator.com/login")
	generated_value = ''.join(random.choice(keyboard_chars) for _ in range(12))
	element = driver.get_element_by_xpath("//input[@type=password and @name='acct'"[0])
	element.send_keys(generated_value)
	element = driver.get_element_by_xpath("//input[@type='text' and @name='pw']"[1])
	element.send_keys(generated_value)
	button = driver.get_element_by_xpath("//input[@type='submit' and @value='create account']")
	button.click()
	print driver.page_source

while (True):
        cur_ip = requests.get("http://icanhazip.com/", proxies={"http": "127.0.0.1:8118"}).text.strip()
        if cur_ip not in ip_list:
                ip_list.append(cur_ip)
                firefox()
                print cur_ip + " | " + generated_value
                print "\n\n"
                print result.text.strip()
                print "\n\n"
        sleep(1)
        with Controller.from_port(port=9051) as controller:
                sleep(1.5)
                controller.authenticate(password="2BV~2B")
                sleep(1.5)
                controller.signal(Signal.NEWNYM)
        sleep(1)

# Keyboard Interrupt

print ("We ended up with " + str(len(ip_list)) + " IP Addresses")
print (ip_list)

def firefox_get(url):
	driver.get(url)
	heading_element = driver.find_element_by_xpath("//*[@id='heading-breadcrumbs']")
	if heading_element:
	    print(heading_element.get_property('textContent').strip())
	else:
	    print("Heading element not found!")


driver.quit()
