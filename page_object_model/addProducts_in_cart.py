from modules import *



def add_products_to_cart(driver,url,product_list,expected_product1,expected_product2):

    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//div[@class='features_items']/h2").text
    assert "FEATURES ITEMS" in home_page_text

    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[2]/a").click()
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH,"//div[@class='features_items']/div[3]/div/div/div[2]")).perform()
    action.move_to_element(driver.find_element(By.XPATH,"//a[@data-product-id='1']")).click().perform()

    wait = WebDriverWait(driver,4)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[text()='Continue Shopping']")))
    time.sleep(2)
    action.move_to_element(driver.find_element(By.XPATH,"//button[text()='Continue Shopping']")).click().perform()

    action.move_to_element(driver.find_element(By.XPATH,"//div[@class='features_items']/div[3]/div/div/div[2]")).perform()
    action.move_to_element(driver.find_element(By.XPATH,"//a[@data-product-id='2']")).click().perform()

    
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[text()='Continue Shopping']")))
    time.sleep(2)
    action.move_to_element(driver.find_element(By.XPATH,"//p[@class='text-center']/a")).click().perform()

    products_in_cart = driver.find_elements(By.XPATH,"//table[@id='cart_info_table']/tbody/tr/td[2]/h4/a")

    products_in_cart_list = []

    for product_ in products_in_cart:
        products_in_cart_list.append(product_.text)


    assert (product_list) == (products_in_cart_list)

    product_1 = {}

    product_1["product_name"]= driver.find_element(By.XPATH,"//table[@id='cart_info_table']//tbody//tr[1]/td[2]/h4/a").text
    product_1["price"]= driver.find_element(By.XPATH,"//table[@id='cart_info_table']//tbody//tr[1]/td[3]/p").text
    product_1["quantity"]= driver.find_element(By.XPATH,"//table[@id='cart_info_table']//tbody//tr[1]/td[4]/button").text
    product_1["total_price"]= driver.find_element(By.XPATH,"//table[@id='cart_info_table']//tbody//tr[1]/td[5]/p").text

    product_2={}
    product_2["product_name"]= driver.find_element(By.XPATH,"//table[@id='cart_info_table']//tbody//tr[2]/td[2]/h4/a").text
    product_2["price"]= driver.find_element(By.XPATH,"//table[@id='cart_info_table']//tbody//tr[2]/td[3]/p").text
    product_2["quantity"]= driver.find_element(By.XPATH,"//table[@id='cart_info_table']//tbody//tr[2]/td[4]/button").text
    product_2["total_price"]= driver.find_element(By.XPATH,"//table[@id='cart_info_table']//tbody//tr[2]/td[5]/p").text

    assert (product_1 == expected_product1 and product_2 == expected_product2) or (
    product_1 == expected_product2 and product_2 == expected_product1)