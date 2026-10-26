from modules import *



def Register_user(driver,url,name,email):
    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//div[@class='features_items']/h2").text
    assert "FEATURES ITEMS" in home_page_text
    
    driver.find_element(By.XPATH,"//div[@class='col-sm-8']/div/ul/li[4]/a").click()
    
    signup_page_text = driver.find_element(By.XPATH,"//div[@class='signup-form']/h2").text
    assert "New User Signup!" in signup_page_text

    driver.find_element(By.XPATH,"//input[@data-qa='signup-name']").send_keys(name)
    driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys(email)

    driver.find_element(By.XPATH,"//button[@data-qa='signup-button']").click()

    wait = WebDriverWait(driver,5)
    
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//p[text()='Email Address already exist!']")))
    register_error = driver.find_element(By.XPATH,"//p[text()='Email Address already exist!']").text
    assert "Email Address already exist!" in register_error
