from time import sleep
import requests
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller
import random

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

while (True):
        cur_ip = requests.get("http://icanhazip.com/", proxies={"http": "127.0.0.1:8118"}).text.strip()
        if cur_ip not in ip_list:
                ip_list.append(cur_ip)
                my_session = requests.session()
                new_account_url = "https://news.ycombinator.com/login?goto=newest"
                generated_value = ''.join(random.choice(keyboard_chars) for _ in range(12))
                result = my_session.get(new_account_url)
                data_ = {
                        "acct": generated_value,
                        "creating": "t",
                        "goto": "newest",
                        "pw": generated_value
                }
                result = my_session.post(
                        "https://news.ycombinator.com/login",
                        data = data_,
                        headers = {
                                "referer": new_account_url,
                                "User-Agent": ua.chrome
                        }
                )
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