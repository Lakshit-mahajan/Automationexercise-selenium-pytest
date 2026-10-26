from modules import *



def view_category_products(driver,url):
    driver.get(url)
    wait = WebDriverWait(driver,11)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='left-sidebar']/h2")))

    category_text = driver.find_element(By.XPATH,"//div[@class='left-sidebar']/h2").text
    assert "CATEGORY" in category_text

    driver.find_element(By.XPATH,"//a[@href='#Women']").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@id='Women']/div/ul/li[2]/a")))
    driver.find_element(By.XPATH,"//div[@id='Women']/div/ul/li[2]/a").click()

    current_url = driver.current_url
    assert "category_products" in current_url
    page_text = driver.find_element(By.XPATH,"//div[@class='features_items']/h2").text
    assert "WOMEN - TOPS PRODUCTS" in page_text

    driver.find_element(By.XPATH,"//a[@href='#Men']").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@id='Men']/div/ul/li[2]/a")))
    driver.find_element(By.XPATH,"//div[@id='Men']/div/ul/li[2]/a").click()
    current_url2 = driver.current_url
    assert "/category_products/6" in current_url2