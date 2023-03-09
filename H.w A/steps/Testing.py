from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

@given(u'that we have gone to {site}')
def step_impl(context, site):
    context.site = site
    context.browser = webdriver.Chrome()
    if not site.startswith("http"):
        site = "https://" + site
    context.browser.get(site)
    time.sleep(5)

@when(u'we search for "{Person}"')
def step_impl(context, Person):
    element_id = "searchInput"
    search_input = context.browser.find_element(By.ID, element_id)
    search_input.clear()
    search_input.send_keys(Person)
    search_input.send_keys(Keys.RETURN)
    time.sleep(5)

@then(u'we find that they worked as "{Occupation}"')
def step_impl(context, Occupation):
    page = context.browser.page_source
    assert Occupation.upper() in page.upper()
