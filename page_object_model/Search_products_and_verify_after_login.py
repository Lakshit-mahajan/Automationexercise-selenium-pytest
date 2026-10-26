from modules import *




def Search_products_and_verify_after_login(driver,url,product_name,email,password):
    driver.get(url)
    time.sleep(4)
    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul/li[2]/a").click()
    products_page = driver.current_url
    assert "/products" in products_page
    driver.find_element(By.ID,"search_product").send_keys(product_name)
    driver.find_element(By.ID,"submit_search").click()

    products = driver.find_elements(By.XPATH,"//div[@class='features_items']//div[@class='col-sm-4']")
    list_of_products_after_search = []
    wait = WebDriverWait(driver,4)
    for product in products:
        list_of_products_after_search.append(product.find_element(By.XPATH,"div/div[1]/div[1]/p").text)
        product.find_element(By.XPATH,"div/div[1]/div/a").click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[text()='Continue Shopping']")))
        driver.find_element(By.XPATH,"//button[text()='Continue Shopping']").click()
    
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='col-sm-8']//ul/li[3]/a")))
    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul/li[3]/a").click()
    cart_url = driver.current_url
    assert "/view_cart" in cart_url

    products_in_the_cart = driver.find_elements(By.XPATH,"//table/tbody/tr")
    product_in_the_cart_list_1 =[]
    for product_in_cart in products_in_the_cart:
        product_in_the_cart_list_1.append(product_in_cart.find_element(By.XPATH,"td[2]/h4/a").text)


    
    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul/li[4]/a").click()
    driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys(email)
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.XPATH,"//button[@data-qa='login-button']").click()

    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='col-sm-8']//ul/li[3]/a")))
    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul/li[3]/a").click()
    
    products_in_the_cart = driver.find_elements(By.XPATH,"//table/tbody/tr")
    product_in_the_cart_list_2 =[]
    for product_in_cart in products_in_the_cart:
        product_in_the_cart_list_2.append(product_in_cart.find_element(By.XPATH,"td[2]/h4/a").text)

    assert product_in_the_cart_list_1 == product_in_the_cart_list_2

