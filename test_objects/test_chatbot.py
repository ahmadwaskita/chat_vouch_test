import re
from page_objects.chatbot import Chatbot

from scripts.helpers import Helpers

from time import sleep

class TestChatbot():
    chatbot = Chatbot()
    helpers = Helpers()

    def test_chatbot_widget(self, driver):
        self.helpers.get_page_main(driver)

        print(driver.current_url)

        btn_widget = self.chatbot.btn_widget_chatbot(driver)

        title_widget = self.chatbot.title_widget(driver)

        avatar_widget = self.chatbot.avatar_widget(driver)
        # avatar_widget_response = self.helpers.check_http_response_no_auth(avatar_widget)

        text_greeting = self.chatbot.text_chatbot_greeting(driver)
        text_date = self.chatbot.text_chatbot_date(driver)
        btn_greeting = self.chatbot.btn_chatbot_greeting(driver)

        print(title_widget.text)
        # print(avatar_widget_response.status_code)
        # print(avatar_widget_response.headers['Content-Type'])
        # print(avatar_widget_response.headers['Content-Length'])
        print(self.helpers.img_response_checker(avatar_widget))
        print(text_greeting.text)
        print(text_date.text)
        print(btn_greeting.text)

        # css style display is dynamic, so the btn_widget (web element) need to be generated at least once
        # before display property shown, and should be updated whenever btn_widget clicked

        btn_widget.click()
        sleep(2)

        img_btn_widget_open = self.chatbot.img_btn_widget_chatbot_open(driver).get_attribute('style')
        img_btn_widget_open_url = self.helpers.regex_findall('"(.+?)"',img_btn_widget_open)[0]
        # img_btn_widget_open_url_response = self.helpers.check_http_response_no_auth(img_btn_widget_open_url)

        img_btn_widget_open_display = self.helpers.regex_findall('display:\s.+[^;]', img_btn_widget_open)[0]

        # print(img_btn_widget_open_url_response.status_code)
        # print(img_btn_widget_open_url_response.headers['Content-Type'])
        print(self.helpers.img_response_checker(img_btn_widget_open_url))
        print(img_btn_widget_open_display)
