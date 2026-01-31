from selenium.webdriver.common.by import By
from behave import given, when, then

FIRST_PRODUCT = (By.CSS_SELECTOR, "a[data-test='product-title']")
ADD_TO_CART_BTN = (
    By.XPATH,
    "//button[.//span[normalize-space()='Add to cart'] or normalize-space()='Add to cart']"
)
VIEW_CART_BTN = (
    By.XPATH,
    "//*[contains(normalize-space(),'View cart') and (self::a or self::button)]"
)
CART_ITEMS = (By.CSS_SELECTOR, "[data-test='cartItem'], [data-test='cart-item']")


@when('Open first product from results')
def open_first_product(context):
    context.driver.find_element(*FIRST_PRODUCT).click()


@when('Add product to cart')
def add_product_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    try:
        context.driver.find_element(*VIEW_CART_BTN).click()
    except:
        context.driver.get('https://www.target.com/cart')


@then('Verify cart has at least {expected_amount} item')
def verify_cart_items(context, expected_amount):
    expected_amount = int(expected_amount)
    items = context.driver.find_elements(*CART_ITEMS)
    visible_items = [i for i in items if i.is_displayed()]
    assert len(visible_items) >= expected_amount, (
        f'Expected at least {expected_amount} item(s), got {len(visible_items)}'
    )