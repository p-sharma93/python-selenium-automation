from operator import and_

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

WAIT = 20

@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def click_cart(context):
    wait = context.wait
    cart_icon = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[aria-label*='cart' i], button[aria-label*='cart' i]")
        )
    )
    cart_icon.click()

@then('Should see "Your cart is empty"')
def verify_empty_cart(context):
    wait = context.wait
    message = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(),'Your cart is empty')]")
        )
    )
    assert "Your cart is empty" in message.text

@when("Click Sign In")
def step_click_sign_in(context):
    wait = context.wait

    sign_in_header = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[normalize-space()='Sign in'] | //button[normalize-space()='Sign in'] | "
                       "//a[normalize-space()='Account'] | //button[normalize-space()='Account']")
        )
    )
    sign_in_header.click()


@then("From the right side navigation menu click Sign In")
def step_click_sign_in_drawer(context):
    wait = context.wait

    sign_in_drawer = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Sign in'] | //a[normalize-space()='Sign in']")
        )
    )
    sign_in_drawer.click()


@then("I should see the Sign In form")
def step_verify_signin_form(context):
    wait = context.wait

    email_input = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
    )
    assert email_input.is_displayed()