from modules import *




def verify_product_page_and_details(driver,url):
    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//div[@class='features_items']/h2").text
    assert "FEATURES ITEMS" in home_page_text

    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[2]/a").click()

    wait = WebDriverWait(driver,4)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h2[text()='All Products']")))

    product_page = driver.find_element(By.XPATH,"//h2[text()='All Products']").text
    assert "ALL PRODUCTS" in product_page


    driver.find_element(By.XPATH,"//div[@class='choose']/ul/li/a").click()

    product_details = {}

    product_details["product_name"] = driver.find_element(By.XPATH,"//div[@class='product-information']/h2").text
    product_details["category"] = driver.find_element(By.XPATH,"//div[@class='product-information']/p[1]").text
    product_details["Availability"] = driver.find_element(By.XPATH,"//div[@class='product-information']/p[2]").text
    product_details["condition"] = driver.find_element(By.XPATH,"//div[@class='product-information']/p[3]").text
    product_details["brand"] = driver.find_element(By.XPATH,"//div[@class='product-information']/p[4]").text

    print(product_details)








