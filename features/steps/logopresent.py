import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('open orange hrm homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify that the logo present on page.')
def step_impl(context):
    time.sleep(5)
    status = context.driver.find_element(By.XPATH, "//div[@class='orangehrm-login-logo']")
    assert status is False


@then('close. browser')
def step_impl(context):
    context.driver.close()