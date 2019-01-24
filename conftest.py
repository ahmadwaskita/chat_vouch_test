import pytest

@pytest.fixture(params=["chrome"], scope="session")
def driver(request):
    from selenium import webdriver
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
        web_driver.maximize_window()

    if request.param == "firefox":
        web_driver = webdriver.Firefox()
        web_driver.maximize_window()

    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", web_driver)
    yield web_driver
    web_driver.close()
    web_driver.quit()