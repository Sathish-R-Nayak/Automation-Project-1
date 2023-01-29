from lib import SeleniumWrapper
from time import sleep
import pytest

headers="fname,lname,add,city,state,zip,ph,ssn,username,password,cpassword"

data=[("Laura","Nayak","Banglore","gulbarga","karnataka",571107,87465673,123,"LAura","Password123","Password123"),
    ("Dora","Gowda","Manglore","mysore","kerala",571109,874650946,321,"DOra","Password321","Password321")]
      


@pytest.mark.parametrize(headers,data)
def test_reg(setup_tear_down,fname,lname,add,city,state,zip,ph,ssn,username,password,cpassword):
    sw=SeleniumWrapper(setup_tear_down)

    sw.click_element(("xpath","//a[text()='Register']"))

    sw.enter_text(("id","customer.firstName"),value=fname)
    sleep(1)
    sw.enter_text(("id","customer.lastName"),value=lname)
    sleep(1)
    sw.enter_text(("id","customer.address.street"),value=add)
    sleep(1)
    sw.enter_text(("id","customer.address.city"),value=city)
    sleep(1)
    sw.enter_text(("id","customer.address.state"),value=state)
    sleep(1)
    sw.enter_text(("id","customer.address.zipCode"),value=zip)
    sleep(1)
    sw.enter_text(("id","customer.phoneNumber"),value=ph)
    sleep(1)
    sw.enter_text(("id","customer.ssn"),value=ssn)
    sleep(1)
    sw.enter_text(("id","customer.username"),value=username)
    sleep(1)
    sw.enter_text(("id","customer.password"),value=password)
    sleep(1)
    sw.enter_text(("id","repeatedPassword"),value=cpassword)
    sleep(1)
    sw.click_element(("xpath","//input[@value='Register']"))
    



    