from selenium import webdriver
from application.application import Application
import pytest

@pytest.fixture
def app(request):
    # Before
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    fixture = Application(driver)
    # request.addfinalizer(fixture.driver.close)

    # After
    def fin():
        # driver.quit()
        pass
    request.addfinalizer(fin)

    return fixture
