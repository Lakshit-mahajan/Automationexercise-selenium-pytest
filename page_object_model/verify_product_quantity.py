from modules import *


def verify_quantity_of_product(driver,url,quantity):
    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//h2[text()='Features Items']").text
    assert "FEATURES ITEMS" in home_page_text

    driver.find_element(By.XPATH,"//a[@href='/product_details/4']").click()

    product_url = driver.current_url

    assert "/product_details" in product_url
    driver.find_element(By.NAME,"quantity").clear()
    driver.find_element(By.NAME,"quantity").send_keys(quantity)
    driver.find_element(By.XPATH,"//button[@type='button']").click()
    wait = WebDriverWait(driver,4)
    wait.until(expected_conditions.visibility_of_any_elements_located((By.XPATH,"//p[@class='text-center']//a")))
    driver.find_element(By.XPATH,"//p[@class='text-center']//a").click()

    quanity_in_cart = driver.find_element(By.XPATH,"//tbody//tr//td[4]/button").text
    assert quantity == int(quanity_in_cart)

