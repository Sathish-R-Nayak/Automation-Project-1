from time import sleep
from selenium.webdriver import Chrome
from pytest import fixture

@fixture(scope="session")
def setup_tear_down():
    driver=Chrome("C:\\chrome\\chromedriver-win32\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://parabank.parasoft.com/parabank/register.htm;jsessionid=E854E23A39712313A7F6A6D668448727")
    sleep(2)
    yield driver
    driver.close()

