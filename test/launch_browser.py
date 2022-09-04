import os
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# source tutorial https://youtu.be/kpONBQ3muLg 

firefox_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0'

firefox_driver = os.path.join(
    os.getcwd(),
    'selenium-drivers/firefox/macos',
    'geckodriver'
    )

firefox_service = Service(firefox_driver)
firefox_options = Options()
firefox_options.set_preference('general.useragent.override',firefox_user_agent)

# launch firefox browser 
browser = webdriver.Firefox(service=firefox_service,options=firefox_options)
browser.get('https://python.org')

