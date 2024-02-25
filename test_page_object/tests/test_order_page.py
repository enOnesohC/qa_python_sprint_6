import pytest
#import allure
import time

from test_page_object.pages.order_page import OrderPage
from ..data import *
from test_page_object.locators.main_page_locators import *
from test_page_object.locators.order_page_locators import *

class TestOrderPage:

    @pytest.mark.parametrize(
        "q_num, expected_result",
        [
            (0, OrderAnswer.ANSWER_0)
        ]
    )
    def test_successful_order(self, driver, q_num, expected_result):
        main_page = OrderPage(driver)
        main_page.take_successful_order(MainPageLocators.BUTTON_ORDER_TOP,
                                        OrderPageLocators.BUTTON_NEXT,
                                        OrderPageLocators.NAME_FIELD,
                                        OrderAnswer.NAME_1,
                                        OrderPageLocators.SECOND_NAME_FIELD,
                                        OrderAnswer.SECOND_NAME_1,
                                        OrderPageLocators.ADRESS_FIELD,
                                        OrderAnswer.ADRESS,
                                        OrderPageLocators.METRO_FIELD,
                                        OrderPageLocators.METRO_STATION,
                                        OrderPageLocators.PHONE_FIELD,
                                        OrderAnswer.PHONE)
        time.sleep(5)





