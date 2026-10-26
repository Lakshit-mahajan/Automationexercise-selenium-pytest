from modules import *




def search_product(driver,url,product_name):
    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//div[@class='features_items']/h2").text
    assert "FEATURES ITEMS" in home_page_text

    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[2]/a").click()
    wait = WebDriverWait(driver,4)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h2[text()='All Products']")))

    driver.find_element(By.ID,"search_product").send_keys(product_name)
    action  = ActionChains(driver)
    action.move_to_element(driver.find_element(By.ID,"submit_search")).click().perform()
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h2[text()='Searched Products']")))

    total_products_after_search = driver.find_elements(By.XPATH,"//div[@class='col-sm-4']/div/div/div/p")
    total_products = 2
    assert total_products == (len(total_products_after_search))