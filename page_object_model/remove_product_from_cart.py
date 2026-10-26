from modules import *


def remove_product_from_cart(driver,url):

    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//h2[text()='Features Items']").text
    assert "FEATURES ITEMS" in home_page_text
    driver.execute_script("window.scrollBy(500,500);")


    driver.find_element(By.XPATH,"//a[@data-product-id='1']/i").click()
    wait = WebDriverWait(driver,4)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='modal-content']/div/h4")))
    added_text = driver.find_element(By.XPATH,"//div[@class='modal-content']/div/h4").text
    assert "Added" in added_text 
    
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='modal-body']/p/a")))
    driver.find_element(By.XPATH,"//div[@class='modal-body']/p/a").click()

    current_url = driver.current_url
    assert "cart" in current_url

    driver.find_element(By.XPATH,"//tr[@id='product-1']/td[6]/a/i").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//b[text()='Cart is empty!']")))
    product_removed_text = driver.find_element(By.XPATH,"//b[text()='Cart is empty!']").text
    assert "Cart is" in product_removed_text