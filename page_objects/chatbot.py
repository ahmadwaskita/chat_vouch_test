from scripts.helpers import Helpers

class Chatbot:

    helpers = Helpers()

    # only page to identified chatbot page objects

    def btn_widget_chatbot(self, driver):
        return self.helpers.wait_clickable_by_id(driver, 'vc-chat-button')

    def img_btn_widget_chatbot_open(self, driver):
        return self.helpers.wait_presence_by_id(driver, 'vc-chat-button-open')

    def img_btn_widget_chatbot_close(self, driver):
        return self.helpers.wait_presence_by_id(driver, 'vc-chat-button-close')

    def title_widget(self, driver):
        return self.helpers.wait_visibility_by_id(driver, 'vc-widget-title')

    def avatar_widget(self, driver):
        return self.helpers.wait_visibility_by_selector(driver, 'img[src="http://files.vouch.sg/5c0899a0f82bb561b4eff07a/1548226022905.jpeg"]').get_attribute('src')

    def text_chatbot_greeting(self, driver):
        return self.helpers.wait_visibility_by_id(driver, 'vc-bubble-no-0')

    def text_chatbot_date(self, driver):
        return self.helpers.wait_visibility_by_class(driver, 'vcw-message-date')

    def btn_chatbot_greeting(self, driver):
        return self.helpers.wait_clickable_by_id(driver, 'vc-greeting-button')

    def chat_messages(self, driver):
        return self.helpers.wait_presence_all_by_class(driver, 'vcw-message-bubble')

    def chat_messages_date(self, driver):
        return self.helpers.wait_presence_all_by_class(driver, 'vcw-message-date')

    def gallery(self, driver):
        return self.helpers.wait_presence_all_by_class(driver, 'vcw-gallery')

    def card_gallery_image(self, driver):
        image = self.helpers.wait_presence_all_by_class(driver, 'vcw-card-image')
        image_src = {}
        for i in image:
            image_src.update({i: i.find_element_by_tag_name('img').get_attribute('src')})
        return image_src

    def card_gallery_title(self, driver):
        return self.helpers.wait_presence_all_by_class(driver, 'vcw-card-text-title')

    def card_gallery_buttons(self, driver):
        buttons = self.helpers.wait_presence_all_by_class(driver, 'vcw-card-button')
        button_text = []
        for i in buttons:
            button_text.append(i.text)
        button_text = list(filter(None, button_text))
        return button_text

    def card_gallery_date(self, driver):
        return self.helpers.wait_presence_all_by_class(driver, 'vcw-message-date-plain')

    def btn_chat_send(self, driver):
        return self.helpers.wait_clickable_by_id(driver, 'vc-btn-send')

    def btn_chat_attach(self, driver):
        return self.helpers.wait_clickable_by_id(driver, 'vc-btn-image')

    def field_chat_text(self, driver):
        return self.helpers.wait_clickable_by_id(driver, 'vc-input')

    def chatbot_quick_replies(self, driver):
        return self.helpers.wait_visibility_all_by_class(driver, 'quick-reply')