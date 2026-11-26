# catalog_page.py
from appium.webdriver.common.appiumby import AppiumBy
from base_page import BasePage
from appium.webdriver.webdriver import WebDriver

ELEMENT_CLICKABLE = "com.saucelabs.mydemoapp.android:id/productIV"
PRODUCTS = (AppiumBy.ID, ELEMENT_CLICKABLE)
ELEMENT_TEXT = "com.saucelabs.mydemoapp.android:id/titleTV"
PRODUCTS_NAME = (AppiumBy.ID, ELEMENT_TEXT)
CART_RESOURCE_ID = "com.saucelabs.mydemoapp.android:id/cartIV"
CART_ELEMENT = (AppiumBy.ID, CART_RESOURCE_ID)
SCROLL_RESOURCE_ID = "com.saucelabs.mydemoapp.android:id/scrollView"
SCROLL_LOCATOR = (AppiumBy.ID, SCROLL_RESOURCE_ID)


class CatalogPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_product(self, index):
        products = self.get_elements(PRODUCTS)
        product = products[index]
        product.click()

    def get_product_name(self, index):
        names = self.get_elements(PRODUCTS_NAME)
        name = names[index]
        return name.text

    def open_cart(self):
        self.click_element(CART_ELEMENT)

    def scroll_catalog(self, max_scrolls=20):
        bottom_reached = self.scroll(SCROLL_LOCATOR, max_scrolls)
        return bottom_reached

    def scroll_to_product(self, name):
        product_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{name}")')
        found = self.scroll_to_element(SCROLL_LOCATOR, product_locator)
        return found

    def open_product_by_name(self, name):
        locator = (AppiumBy.XPATH, f'//android.widget.TextView[@text="{name}"]/../android.widget.ImageView[@content-desc="Product Image"]')
        self.scroll_to_element(SCROLL_LOCATOR, locator)
        self.click_element(locator)