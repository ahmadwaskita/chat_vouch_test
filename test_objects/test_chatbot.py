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
        print('assert title_widget pass')

        assert self.helpers.img_response_checker(avatar_widget) == 'image_ok'
        print('assert avatar_widget pass')

        assert text_greeting.text == 'Hi, come chat with us!'
        print('assert text_greeting pass')

        # assert date
        assert text_date.text[:-9] == internet_date[:-9]
        print('assert text_date pass')

        # assert time delta less than a minute
        assert self.helpers.time_delta_one_minute(internet_date, text_date.text) is True
        print('assert time_delta_one_minute(internet_date, text_date) pass')

        assert btn_greeting.text == 'Get Started'
        print('assert btn_greeting pass')

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
        print('assert img_btn_widget_open_url pass')

        assert self.helpers.img_response_checker(img_btn_widget_close_url) == 'image_ok'
        print('assert img_btn_widget_close_url pass')

        '''
        condition for chatbot widget button opened
        - img_btn_widget_open_display : block
        - img_btn_widget_close_display : none
        '''
        assert img_btn_widget_open_display[9:] == 'none'
        print('assert img_btn_widget_open hidden pass')

        assert img_btn_widget_close_display[9:-12] == 'block'
        print('assert img_btn_widget_close shown pass')

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

        assert img_btn_widget_open_display[9:] == 'block'
        print('assert img_btn_widget_open shown pass')

        assert img_btn_widget_close_display[9:-12] == 'none'
        print('assert img_btn_widget_close hidden pass')

    def test_chatbot_input_interactive(self, driver):
        driver.refresh()
        self.helpers.get_page_main(driver)

        btn_greeting = self.chatbot.btn_chatbot_greeting(driver)
        btn_greeting.click()
        print('btn greeting clicked')

        sleep(10)

        gallery = self.chatbot.gallery(driver)

        chat_messages = self.chatbot.chat_messages(driver)

        # chat_date = self.chatbot.chat_messages_date(driver)

        gallery_image = self.chatbot.card_gallery_image(driver)

        gallery_image_keys = list(gallery_image.keys())
        # gallery_image_values = list(gallery_image.values())

        # gallery_title = self.chatbot.card_gallery_title(driver)

        # gallery_buttons = self.chatbot.card_gallery_buttons(driver)

        self.helpers.scroll_to_element(driver, chat_messages[0])
        sleep(3)
        print('scrolled to first message')

        self.helpers.scroll_to_element(driver, gallery[0])
        sleep(3)
        print('scrolled to gallery card')

        self.helpers.scroll_to_element(driver, gallery_image_keys[4])
        sleep(3)
        print('scrolled to last gallery image')

        self.helpers.scroll_to_element(driver, gallery_image_keys[0])
        sleep(3)
        print('scrolled to first gallery image')

        # gallery_date = self.chatbot.card_gallery_date(driver)

    def test_chatbot_input_unknown_words(self, driver):
        driver.refresh()
        self.helpers.get_page_main(driver)

        # btn_greeting = self.chatbot.btn_chatbot_greeting(driver)
        # btn_greeting.click()
        #
        # sleep(10)

        field_chat_text = self.chatbot.field_chat_text(driver)
        btn_chat_attach = self.chatbot.btn_chat_attach(driver)
        btn_chat_send = self.chatbot.btn_chat_send(driver)

        field_chat_text.click()
        self.helpers.send_text(field_chat_text, 'a')
        btn_chat_send.click()

        sleep(3)

        chat_messages = self.chatbot.chat_messages(driver)

        chat_date = self.chatbot.chat_messages_date(driver)

        conversation_length = len(chat_messages)

        conversation_1_text = chat_messages[conversation_length-2:]
        conversation_1_date = chat_date[conversation_length-2:]

        conversation_1 = dict(zip(conversation_1_text, conversation_1_date))

        for k,v in conversation_1.items():
            print(k.text, v.text)

        # assert user input
        assert conversation_1_text[0].text == "a"
        print('assert user input pass')

        # assert chatbot response
        assert conversation_1_text[1].text == "Sorry, I didn't get that. Could you try saying it in a different way?"
        print('assert chatbot response pass')


    def test_chatbot_input_known_words(self, driver):
        driver.refresh()
        self.helpers.get_page_main(driver)

        # btn_greeting = self.chatbot.btn_chatbot_greeting(driver)
        # btn_greeting.click()
        #
        # sleep(10)

        field_chat_text = self.chatbot.field_chat_text(driver)
        btn_chat_attach = self.chatbot.btn_chat_attach(driver)
        btn_chat_send = self.chatbot.btn_chat_send(driver)

        field_chat_text.click()
        self.helpers.send_text(field_chat_text, 'food')
        btn_chat_send.click()

        sleep(3)

        chat_messages = self.chatbot.chat_messages(driver)

        chat_date = self.chatbot.chat_messages_date(driver)

        conversation_length = len(chat_messages)

        conversation_1_text = chat_messages[conversation_length - 2:]
        conversation_1_date = chat_date[conversation_length - 2:]

        conversation_1 = dict(zip(conversation_1_text, conversation_1_date))

        for k, v in conversation_1.items():
            print(k.text, v.text)

        # assert user input
        assert conversation_1_text[0].text == "food"
        print('assert user input pass')

        # assert chatbot response
        assert conversation_1_text[1].text == "Are you looking to eat within Andaz or around the area?"
        print('assert chatbot response pass')

        chatbot_quick_reply = self.chatbot.chatbot_quick_replies(driver)

        # assert chatbot response for input word 'food'
        assert chatbot_quick_reply[0].text == "In-house"
        print('assert button quick reply pass')

        assert chatbot_quick_reply[1].text == "Around the area"
        print('assert button quick reply pass')

        assert chatbot_quick_reply[2].text == "I'm at the pool"
        print('assert button quick reply pass')


