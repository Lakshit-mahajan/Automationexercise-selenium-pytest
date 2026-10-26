from modules import *


def Logout_user(driver,url,email,password,name):

    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//div[@class='features_items']/h2").text
    assert "FEATURES ITEMS" in home_page_text
    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[4]/a").click()

    login_page_text = driver.find_element(By.XPATH,"//div[@class='login-form']//h2").text
    assert "Login to your account" in login_page_text
    driver.find_element(By.XPATH,"//form[@action='/login']/input[2]").send_keys(email)
    driver.find_element(By.XPATH,"//form[@action='/login']/input[3]").send_keys(password)
    driver.find_element(By.XPATH,"//form[@action='/login']/button").click()

    after_login_text = driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[10]/a").text
    assert f"Logged in as {name}" in after_login_text
    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul/li[4]/a").click()

    page_url = driver.current_url
    assert "login" in page_url