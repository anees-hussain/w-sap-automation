import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
import pywhatkit as pwk
import login # Login Module

# Providing options to leave browser open after program complete
options = Options()
options.add_experimental_option("detach", True)

# Connection to VPN (Pulse Secure)
login.pulseSecureConnection()

# Launching Chrome Browser Instance
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Logging into target website
login.loginToWebsap(driver)

# Provides Balance Screenshot
driver.find_element("xpath", "//div[@class='panel-body']").screenshot("C:/Users/HP/OneDrive/Desktop/balance.png")

# .screenshot("C:/Users/HP/OneDrive/Desktop/s.png")
driver.find_element("xpath", "//a[@class='btn btn-sm btn-success']").click()

sleep(10)
# Provides Rows of all orders Screenshot
driver.find_element("xpath", "//tbody[@role='rowgroup']").screenshot("C:/Users/HP/OneDrive/Desktop/websap-orders.png")

pwk.sendwhats_image("+923003304931", "C:/Users/HP/OneDrive/Desktop/balance.png")
pwk.sendwhats_image("+923003304931", "C:/Users/HP/OneDrive/Desktop/websap-orders.png")

os.remove("C:/Users/HP/OneDrive/Desktop/balance.png")
sleep(3)
os.remove("C:/Users/HP/OneDrive/Desktop/websap-orders.png")

driver.quit()