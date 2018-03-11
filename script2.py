import os
import sys

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

os.environ["MOZ_HEADLESS"]="1"

binary = FirefoxBinary("/usr/lib/firefox/firefox", log_file=sys.stdout)

driver = webdriver.Firefox(firefox_binary=binary)

driver.get("https://intoli.com/blog/running-selenium-with-headless-firefox/")

heading_element = driver.find_element_by_xpath("//*[@id='heading-breadcrumbs']")

if heading_element:
    print(heading_element.get_property('textContent').strip())
else:
    print("Heading element not found!")

driver.quit()
