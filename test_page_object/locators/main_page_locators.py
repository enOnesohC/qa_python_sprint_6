from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, "//div[@id='accordion__heading-{}']"
    ANSWER_LOCATOR = By.XPATH, "//div[@id='accordion__panel-{}']"
    BUTTON_ORDER_TOP = By.XPATH, "//button[@class='Button_Button__ra12g']"
    BUTTON_ORDER_BOTTOM = By.XPATH, "//button[@class='Button_Button__ra12g.Button_Middle__1CSJM']"
