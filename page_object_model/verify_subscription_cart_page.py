from modules import *




def verify_subsciption_cart_page(driver,url,email):
    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//h2[text()='Features Items']").text
    assert "FEATURES ITEMS" in home_page_text

    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[3]/a").click()
    driver.execute_script("window.scrollBy(600,600);")
    driver.find_element(By.ID,"susbscribe_email").send_keys(email)
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.ID,"subscribe")).click().perform()
    wait = WebDriverWait(driver,4)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@id='success-subscribe']/div")))
    success_text = driver.find_element(By.XPATH,"//div[@id='success-subscribe']/div").text
    assert "successfully subscribed!" in success_text