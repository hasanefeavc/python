import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I launch Chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome()


@when('I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("user")
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("pwd")


@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()



@then('User must successfully login to the Dashboard page')
def step_impl(context):
    time.sleep(1)
