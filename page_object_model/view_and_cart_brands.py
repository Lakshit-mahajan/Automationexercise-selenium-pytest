from modules import *




def view_and_cart_products(driver,url):
    driver.get(url)
    driver.find_element(By.XPATH,"//div[@class='col-sm-8']/div/ul/li[2]/a").click()
    driver.execute_script("window.scrollBy(600,600);")
    wait = WebDriverWait(driver,4)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='brands_products']/h2")))
    brand_text = driver.find_element(By.XPATH,"//div[@class='brands_products']/h2").text
    assert "BRANDS" in brand_text
    driver.find_element(By.XPATH,"//a[@href='/brand_products/Biba']").click()
    assert "/brand_products/Biba" in driver.current_url

    driver.find_element(By.XPATH,"//a[@href='/brand_products/H&M']").click()
    assert "/brand_products/H&M" in driver.current_url


    

    

    # time.sleep(10)