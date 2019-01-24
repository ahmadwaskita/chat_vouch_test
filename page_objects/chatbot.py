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