from modules import *




def verify_subscription_home_page(driver,url,email):
    driver.get(url)
    driver.execute_script("window.scrollBy(8000,8000);")
    driver.find_element(By.ID,"susbscribe_email").send_keys(email)
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.ID,"subscribe")).click().perform()
    wait = WebDriverWait(driver,4)
    
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@id='success-subscribe']/div")))
    success_text = driver.find_element(By.XPATH,"//div[@id='success-subscribe']/div").text
    assert "successfully subscribed!" in success_text