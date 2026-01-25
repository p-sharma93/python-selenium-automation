from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/your-account/order-history?ref_=ya_d_c_yo')
sleep(2)

#Amazon logo (presence check)
driver.find_element(By.CLASS_NAME, "a-link-nav-icon")

#Email field
driver.find_element(By.ID, "ap_email")


#Continue button
driver.find_element(By.ID, "continue")

#Conditions of use link
driver.find_element(By.LINK_TEXT, "Conditions of Use")

#Privacy Notice link
driver.find_element(By.LINK_TEXT, "Privacy Notice")

#Need help link
driver.find_element(By.LINK_TEXT, "Need help?")

#Forgot your password link
driver.find_element(By.ID, "auth-fpp-link-bottom")

#Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link")

#Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")

driver.quit()