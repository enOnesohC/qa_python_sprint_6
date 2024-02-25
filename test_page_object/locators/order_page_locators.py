from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = By.XPATH, "//input[@placeholder='* Имя']"
    SECOND_NAME_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADRESS_FIELD = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    PHONE_FIELD = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    METRO_FIELD = By.XPATH, "//input[@placeholder='* Станция метро']"
    METRO_STATION = By.XPATH, "//input[@value='Сокольники']"

    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']"

    DAY_ORDER = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    RENT = By.XPATH, "//div[@class='Dropdown-root.Order_FilledDate__1pb8n']"
    COLOR_BLACK = By.XPATH, "//input[@id='black']"
    COLOR_GREY = By.XPATH, "//input[@id='grey']"
    COMMENTARY = By.XPATH, "//input[@placeholder='Комментарий для курьера']"

    BUTTON_ORDER = By.XPATH, "//button[@class='Button_Button__ra12g.Button_Middle__1CSJM']"

    BUTTON_CONFIRMED_YES = By.XPATH, "//button[text()='Да']"
    BUTTON_CONFIRMED_NO = By.XPATH, "//button[text()='Нет']"

    ORDER_MESSAGE = By.XPATH, "//div[text()='Заказ оформлен']"
    BUTTON_STATUS = By.XPATH, "//button[text()='Посмотреть статус']"

    LOGO_SCOOTER = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"
    LOGO_YANDEX = By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"
