from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

UNLOCK_HEADER = (By.XPATH, "//*[normalize-space()='Unlock added value']")
STORY_CARDS = (
    By.XPATH,
    "//*[normalize-space()='Unlock added value']/ancestor::*[self::section or self::div][1]//a"
)


@given('Open Target Circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle')
    context.wait.until(EC.presence_of_element_located(UNLOCK_HEADER))


@then('Verify {expected_amount} story cards under Unlock added value are shown')
def verify_story_cards(context, expected_amount):
    expected_amount = int(expected_amount)

    context.wait.until(EC.presence_of_element_located(UNLOCK_HEADER))
    context.wait.until(EC.presence_of_all_elements_located(STORY_CARDS))

    cards = context.driver.find_elements(*STORY_CARDS)
    visible_cards = [c for c in cards if c.is_displayed()]
    assert len(visible_cards) == expected_amount, (
        f'Expected {expected_amount} cards, got {len(visible_cards)}'
    )