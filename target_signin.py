from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open url
driver.get('https://www.target.com/')
sleep(5)

# Click account button
driver.find_element(By.ID, "account-sign-in").click()
sleep(2)

# Click SignIn btn from side navigation
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
sleep(2)

# Verify SignIn page opened:
driver.find_element(By.XPATH, "//*[contains(text(), 'Sign in or create account')]")
driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")


driver.quit()