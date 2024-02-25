from test_page_object.pages.base_page import BasePage
from test_page_object.locators.main_page_locators import MainPageLocators


class OrderPage(BasePage):
    def take_successful_order(self,
                              locator_button_order,
                              locator_button_next,
                              name_locator,
                              name,
                              second_name_locator,
                              second_name,
                              adress_locator,
                              adress,
                              metro_locator,
                              metro,
                              phone_locator,
                              phone
                              ):
        OrderPage.push_buttor_order(self, locator_button_order)
        OrderPage.first_fil(self,
                            name_locator,
                            name,
                            second_name_locator,
                            second_name,
                            adress_locator,
                            adress,
                            metro_locator,
                            metro,
                            phone_locator,
                            phone)
        OrderPage.push_button_next(self, locator_button_next)
        OrderPage.second_fil(self)
        OrderPage.push_buttor_order(self, locator_button_order)

    def push_buttor_order(self, locator_button_order):
        method_q, locator_q = locator_button_order
        self.click_on_element((method_q, locator_q))

    def push_button_next(self, locator_button_next):
        method_q, locator_q = locator_button_next
        self.click_on_element((method_q, locator_q))

    def first_fil(self,
                  name_locator,
                  name,
                  second_name_locator,
                  second_name,
                  adress_locator,
                  adress,
                  metro_locator,
                  metro_station_locator,
                  phone_locator,
                  phone):
        method_q, locator_q = name_locator
        self.set_text_to_element((method_q, locator_q), name)

        method_q, locator_q = second_name_locator
        self.set_text_to_element((method_q, locator_q), second_name)

        method_q, locator_q = adress_locator
        self.set_text_to_element((method_q, locator_q), adress)

        method_q, locator_q = metro_locator
        self.click_on_element((method_q, locator_q))

        method_q, locator_q = metro_station_locator
        #self.click_on_element((method_q, locator_q))
        element = self.find_element_with_wait((method_q, locator_q))
        self.driver.execute_script("arguments[0].value = 'Сокольники';", element)

        method_q, locator_q = phone_locator
        self.set_text_to_element((method_q, locator_q), phone)

    def second_fil(self):
        pass