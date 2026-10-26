from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
from selenium.webdriver import ActionChains
import os



@pytest.mark.test_automation
def test_automation():
    driver = webdriver.Firefox()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.find_element(By.ID,"autocomplete").send_keys("Ind")
    time.sleep(5)
    countries = driver.find_elements(By.XPATH,"//ul[@id='ui-id-1']/li")
    for country in countries:
        if country.text == "India":
            country.click()

    Select_c = Select(driver.find_element(By.ID,"dropdown-class-example"))
    Select_c.select_by_value("option2")

    
    
