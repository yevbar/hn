import os
import sys

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

os.environ["MOZ_HEADLESS"]="1"
binary = FirefoxBinary("/usr/lib/firefox/firefox", log_file=sys.stdout)
driver = webdriver.Firefox(firefox_binary=binary)

def firefox_get(url):
	driver.get(url)
	element = driver.find_element_by_name("acct").send_keys("Zach-Latta")
	element = driver.find_element_by_name("pw").send_keys("Latta Love")
	button = driver.find_element_by_xpath("//input[@type='submit' and @value='create account']")
	button.click()
	print driver.page_source

firefox_get("https://news.ycombinator.com/login")

driver.quit()
