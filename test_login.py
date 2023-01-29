from lib import SeleniumWrapper
from time import sleep
import pytest

headers="Username,Password"

data=[("sathish","password1234"),("nithish","password5678"),("jithish","password9876")]

@pytest.mark.parametrize(headers,data)
def test_login(setup_tear_down,Username,Password):

    sw=SeleniumWrapper(setup_tear_down)

    sw.enter_text(("name","username"),value=Username)
    sleep(1)
    sw.enter_text(("name","password"),value=Password)
    sleep(1)
    sw.click_element(("xpath","(//input[@class='button'])[1]"))
    


