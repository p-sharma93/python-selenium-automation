from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Start Chrome browser:
driver.get('https://stackoverflow.com/users/signup')


CREATE_ACCOUNT_HEADER = (By.XPATH, "//h1[normalize-space()='Create your account']")

EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")

PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")

SIGN_UP_BUTTON = (By.XPATH, "//button[normalize-space()='Sign up']")

GOOGLE_SIGN_UP = (By.XPATH, "//button[contains(normalize-space(),'Google')]")

GITHUB_SIGN_UP = (By.XPATH, "//button[contains(normalize-space(),'GitHub')]")

TEAMS_PROMO_LINK = (By.CSS_SELECTOR, "a[href*='/teams']")

