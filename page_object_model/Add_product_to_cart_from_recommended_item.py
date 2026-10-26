from modules import *



def Add_product_to_cart_from_recommended_item(driver,url):
    driver.get(url)
    driver.execute_script("window.scrollBy(8000,8000);")
    product_name = driver.find_element(By.XPATH,"//div[@class='item active']/div/div/div/div/p").text
    driver.find_element(By.XPATH,"//div[@class='item active']/div/div/div/div/a").click()
    wait = WebDriverWait(driver,4)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//u[text()='View Cart']")))
    driver.find_element(By.XPATH,"//u[text()='View Cart']").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//td[@class='cart_description']/h4/a")))
    product_name_in_cart = driver.find_element(By.XPATH,"//td[@class='cart_description']/h4/a").text
    assert product_name == product_name_in_cart
