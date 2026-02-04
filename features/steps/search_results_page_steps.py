from selenium.webdriver.common.by import By
from behave import when, then

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_IMG = (By.CSS_SELECTOR, "img")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    products = context.driver.find_elements(*LISTINGS)
    for product in products[:8]:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(f'{title}')
        product.find_element(*PRODUCT_IMG)
