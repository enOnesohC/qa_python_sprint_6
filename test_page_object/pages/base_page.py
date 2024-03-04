from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def find_element_with_wait(self, locator):
        (WebDriverWait(self.driver, 5).
         until(expected_conditions.visibility_of_element_located(locator)))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element.text

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.send_keys(text)

    def click_java(self, locator):
        js = "arguments[0].click();"
        button = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].click();", button)

    def switch_modal(self, locator):
        modal = self.find_element_with_wait(locator)
        self.driver.switch_to.frame(modal)
