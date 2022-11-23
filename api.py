import pandas as pd
import requests
from selenium.webdriver.common.by import By

response = requests.get("https://free-proxy-list.net/%22)

# List proxys usable
proxy_list = pd.read_html(response.text)[0]
proxy_list["url"] = "http://" + proxy_list["IP Address"] + ":" + proxy_list["Port"].astype(str)
proxy_list.head()

# Count proxys that use https only
https_proxies = proxy_list[proxy_list["Https"] == "yes"]
https_proxies.count()

# Log to the account fakejson
login_data = {
        '_csrf_token':'Z0ZCLRcjfjsaSgV4WywHAW00eT8PCQULS0qYXFOrOyKH1EnCYA4t6hby',
        'session[email]': 'test@gmail.com',
        'session[password]':'test',
        'session[remember_me]':'false'
    }

# Payload of the mock api
payload ={
  "token": "3nFywF-DZkofHe3PTZQV0Q",
  "data": {
    "id": "personNickname",
    "last_login": {
      "date_time": "dateTime|UNIX",
      "ip4": "internetIP4"
    }
  }
}


url = "https://app.fakejson.com/q"
url1 = 'https://app.fakejson.com/auth/sessions/new'
na = 'test@gmail.com'
pa = 'test'

# Set proxys useable on a list stoping at 5 proxys
good_proxies = set()
for proxy_url in https_proxies["url"]:
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }

    try:
        response = requests.get(url, json = payload, proxies=proxies, timeout=2)
        good_proxies.add(proxy_url)
        print(f"Proxy {proxy_url} Add")
    except Exception:
        pass

    if len(good_proxies) >=5:
        break

from selenium import webdriver

# with requests.Session() as s:

#     s.get(url1)

#     if login_data.ok:
#         print('conected')
#     else:
#         print('non')

# connect to the URl using good_proxies
for proxy_url in good_proxies:
    proxy = proxy_url.replace("http://", "")

    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True

    firefox_capabilities['proxy'] = {
        "proxyType": "MANUAL",
        "httpProxy": proxy,
        "sslProxy": proxy
    }



    driver = webdriver.Firefox(capabilities=firefox_capabilities)



    # driver.find_element("session[email]").send_keys(na)
    # driver.find_element("session[password]]").send_keys(pa)
    # driver.find_element(".c-btn").click()

    print("tu es connecté")

    #  add my account by element using webdriver

    driver.get("https://app.fakejson.com/auth/sessions/new%22)
username =  driver.find_element(By.ID, "session[email]").send_keys(na)
# username.send_keys(na)
password = driver.find_element_by_id(By.ID, "session[password]]").send_keys(pa)
# password.send_keys(pa)
button = driver.find_element_by_class_name(By.CLASS_NAME, "c-btn c-btn--info c-btn--fullwidth").click()
# button.click()

print("tu es connecté")