from modules import *



def Add_review_on_product(driver,url,name,email,review):
    driver.get(url)
    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[2]/a").click()
    product_page_url= driver.current_url
    assert "https://automationexercise.com/products" in product_page_url
    driver.find_element(By.XPATH,"//a[@href='/product_details/2']").click()
    driver.execute_script("window.scrollBy(500,500);")
    wait = WebDriverWait(driver,4)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//a[text()='Write Your Review']")))
    driver.find_element(By.ID,"name").send_keys(name)
    driver.find_element(By.ID,"email").send_keys(email)
    driver.find_element(By.ID,"review").send_keys(review)
    driver.find_element(By.ID,"button-review").click()
    wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH,"//span[text()='Thank you for your review.']")))
    success_text = driver.find_element(By.XPATH,"//span[text()='Thank you for your review.']").text
    assert "Thank you for your review." in success_text

