from selenium.webdriver.common.by import By


def get_email_field(driver):
    return driver.find_element(By.ID, "signup-email")


def get_password_field(driver):
    return driver.find_element(By.ID, "signup-password")


def get_first_name_field(driver):
    return driver.find_element(By.ID, "signup-first_name")


def get_last_name_field(driver):
    return driver.find_element(By.ID, "signup-last_name")


def get_city_field(driver):
    return driver.find_element(By.ID, "signup-city")


def get_address_field(driver):
    return driver.find_element(By.ID, "signup-address")


def get_zip_code_field(driver):
    return driver.find_element(By.ID, "signup-zip_code")


def get_phone_field(driver):
    return driver.find_element(By.ID, "signup-phone")


def get_save_button(driver):
    return driver.find_element(By.CLASS_NAME, "btn-primary")


