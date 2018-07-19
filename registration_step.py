from registration_objects import *

'''Better to make email autogeneration it will help not to get "Mail already exist" message'''


def registration(driver, email="test@t.tt", password="qwerty", first_name="Dima", last_name="DimaTest", city="Kiev",
                 address="Mayakovskogo str", zip_code="02225", phone="1234567"):
    get_email_field(driver).send_keys(email)
    get_password_field(driver).send_keys(password)
    get_first_name_field(driver).send_keys(first_name)
    get_last_name_field(driver).send_keys(last_name)
    get_city_field(driver).send_keys(city)
    get_address_field(driver).send_keys(address)
    get_zip_code_field(driver).send_keys(zip_code)
    get_phone_field(driver).send_keys(phone)
    get_save_button(driver).click()


"""Also better to make text checker for every type of message, and use PARTIAL_LINK_TEXT to catch all messages
Because now it just looks for element with classname = help-block (All alert message for all fields)
Better to separate them all"""


def help_block(driver):
    return driver.find_element(By.CLASS_NAME, "help-block")


def is_user_created(driver):
    return driver.find_element(By.PARTIAL_LINK_TEXT, "User has been successfully added")
