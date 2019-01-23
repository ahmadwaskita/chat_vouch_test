import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# from selenium import webdriver

# @pytest.fixture(scope="class")
# def browser():
#     with webdriver.Chrome() as browser:
#         yield browser


# @pytest.fixture(params=["chrome", "firefox"],scope="session")
@pytest.fixture(params=["chrome"], scope="session")
def driver(request):
    from selenium import webdriver
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
        web_driver.maximize_window()
        # web_driver.set_window_position(0, 0)
        # web_driver.set_window_size(1920, 1080)
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
        web_driver.maximize_window()
        # web_driver.set_window_position(0, 0)
        # web_driver.set_window_size(1920, 1080)
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", web_driver)
    yield web_driver
    web_driver.close()
    web_driver.quit()