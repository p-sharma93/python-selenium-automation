from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PRODUCT_URL = "https://www.target.com/p/A-91511634"

COLOR_LABEL = (By.XPATH, "//*[contains(normalize-space(),'Color')]")
COLOR_OPTIONS = (By.XPATH, "//*[contains(normalize-space(),'Color')]/ancestor::*[1]//*[@role='radio']")
SELECTED_RADIO = (
    By.XPATH,
    "//*[contains(normalize-space(),'Color')]/ancestor::*[1]//*[@role='radio' and @aria-checked='true']"
)

CLOSE_POPUP = (
    By.CSS_SELECTOR,
    "button[aria-label='close'], button[aria-label='Close'], button[data-test='close-button']"
)


@given('Open Target product page A-91511634')
def open_product_page(context):
    context.driver.get(PRODUCT_URL)

    try:
        context.driver.wait.until(EC.element_to_be_clickable(CLOSE_POPUP)).click()
    except:
        pass

    context.driver.wait.until(EC.presence_of_element_located(COLOR_LABEL))
    context.driver.wait.until(EC.presence_of_all_elements_located(COLOR_OPTIONS))


@then('Click each color and verify it is selected')
def click_each_color_and_verify_selected(context):
    options = context.driver.find_elements(*COLOR_OPTIONS)
    options = [o for o in options if o.is_displayed()]

    assert len(options) > 1, f"Expected multiple color options, got {len(options)}"

    for option in options:
        context.driver.wait.until(EC.element_to_be_clickable(option)).click()

        selected = context.driver.find_elements(*SELECTED_RADIO)
        assert len(selected) >= 1, "No selected color option detected after clicking"