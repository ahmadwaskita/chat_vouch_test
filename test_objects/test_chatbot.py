from page_objects.chatbot import Chatbot

from scripts.helpers import Helpers

from time import sleep


class TestChatbot():
    chatbot = Chatbot()
    helpers = Helpers()

    def test_chatbot_widget(self, driver):
        self.helpers.get_page_main(driver)

        # print(driver.current_url)

        title_widget = self.chatbot.title_widget(driver)
        avatar_widget = self.chatbot.avatar_widget(driver)
        text_greeting = self.chatbot.text_chatbot_greeting(driver)
        internet_date = self.helpers.internet_time()
        text_date = self.chatbot.text_chatbot_date(driver)
        btn_greeting = self.chatbot.btn_chatbot_greeting(driver)

        # print(title_widget.text)
        # print(self.helpers.img_response_checker(avatar_widget))
        # print(text_greeting.text)
        # print(text_date.text)
        # print(internet_date)
        # print(btn_greeting.text)

        assert title_widget.text == 'Vouch Widget'
        assert self.helpers.img_response_checker(avatar_widget) == 'image_ok'
        assert text_greeting.text == 'Hi, come chat with us!'

        # assert date
        assert text_date.text[:-9] == internet_date[:-9]

        # assert time delta less than a minute
        assert self.helpers.time_delta_one_minute(internet_date, text_date.text) is True

        assert btn_greeting.text == 'Get Started'

        '''
        css style display is dynamic, so the btn_widget (web element) need to be generated at least once
        before display property shown, and should be updated whenever btn_widget clicked
        '''
        btn_widget = self.chatbot.btn_widget_chatbot(driver)

        img_btn_widget_open = self.chatbot.img_btn_widget_chatbot_open(driver).get_attribute('style')
        img_btn_widget_open_url = self.helpers.regex_findall('"(.+?)"',img_btn_widget_open)[0]
        img_btn_widget_open_display = self.helpers.regex_findall('display:\s.+[^;]', img_btn_widget_open)[0]

        img_btn_widget_close = self.chatbot.img_btn_widget_chatbot_close(driver).get_attribute('style')
        img_btn_widget_close_url = self.helpers.regex_findall('"(.+?)"',img_btn_widget_close)[0]
        img_btn_widget_close_display = self.helpers.regex_findall('display:\s.+[^;]', img_btn_widget_close)[0]

        # print(self.helpers.img_response_checker(img_btn_widget_open_url))
        # print(img_btn_widget_open_display[9:])
        # print(img_btn_widget_close_display[9:-12])

        assert self.helpers.img_response_checker(img_btn_widget_open_url) == 'image_ok'
        assert self.helpers.img_response_checker(img_btn_widget_close_url) == 'image_ok'

        '''
        condition for chatbot widget button opened
        - img_btn_widget_open_display : block
        - img_btn_widget_close_display : none
        '''
        assert img_btn_widget_open_display[9:] == 'none'
        assert img_btn_widget_close_display[9:-12] == 'block'

        btn_widget.click()
        sleep(2)

        '''
        remember > update dynamic element after click
        condition for chatbot widget button closed
        - img_btn_widget_open_display : block
        - img_btn_widget_close_display : none
        '''

        img_btn_widget_open = self.chatbot.img_btn_widget_chatbot_open(driver).get_attribute('style')
        img_btn_widget_open_display = self.helpers.regex_findall('display:\s.+[^;]', img_btn_widget_open)[0]

        img_btn_widget_close = self.chatbot.img_btn_widget_chatbot_close(driver).get_attribute('style')
        img_btn_widget_close_display = self.helpers.regex_findall('display:\s.+[^;]', img_btn_widget_close)[0]

        # print(self.helpers.img_response_checker(img_btn_widget_close_url))
        # print(img_btn_widget_open_display[9:])

        assert img_btn_widget_open_display[9:] == 'block'
        assert img_btn_widget_close_display[9:-12] == 'none'

    def test_chatbot_input_interactive(self, driver):
        driver.refresh()
        self.helpers.get_page_main(driver)

        print(driver.current_url)

        btn_greeting = self.chatbot.btn_chatbot_greeting(driver)
        btn_greeting.click()

        sleep(5)

    def test_chatbot_input_unknown_words(self, driver):
        driver.refresh()
        self.helpers.get_page_main(driver)

        print(driver.current_url)

        btn_greeting = self.chatbot.btn_chatbot_greeting(driver)
        btn_greeting.click()
        pass

    def test_chatbot_input_known_words(self, driver):
        driver.refresh()
        self.helpers.get_page_main(driver)

        print(driver.current_url)

        btn_greeting = self.chatbot.btn_chatbot_greeting(driver)
        btn_greeting.click()
        pass

