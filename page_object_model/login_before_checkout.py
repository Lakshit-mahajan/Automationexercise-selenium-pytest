from modules import *


def login_before_checkout(driver,url,name,email,password,address,comment,name_on_card,card_number,cvc,e,year):
    driver.implicitly_wait(5)
    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//h2[text()='Features Items']").text
    assert "FEATURES ITEMS" in home_page_text

    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[4]/a").click()
    driver.find_element(By.XPATH,"//form[@action='/login']/input[2]").send_keys(email)
    driver.find_element(By.XPATH,"//form[@action='/login']/input[3]").send_keys(password)
    driver.find_element(By.XPATH,"//form[@action='/login']/button").click()

    after_login_text = driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[10]/a").text
    assert f"Logged in as {name}" in after_login_text

    driver.find_element(By.XPATH,"//a[@data-product-id='2']").click()
    driver.find_element(By.XPATH,"//a[@href='/view_cart']/u").click()
    
    cart_page_url = driver.current_url
    assert "/view_cart" in cart_page_url
    driver.find_element(By.XPATH,"//a[text()='Proceed To Checkout']").click()
    address_1 = driver.find_element(By.XPATH,"//ul[@id='address_delivery']//li[4]").text
    assert address in  address_1
    driver.find_element(By.NAME,"message").send_keys(comment)
    driver.find_element(By.XPATH,"//a[text()='Place Order']").click()
    driver.find_element(By.NAME,"name_on_card").send_keys(name_on_card)
    driver.find_element(By.NAME,"card_number").send_keys(card_number)
    driver.find_element(By.NAME,"cvc").send_keys(cvc)
    driver.find_element(By.NAME,"expiry_month").send_keys(year)
    driver.find_element(By.NAME,"expiry_year").send_keys(2090)
    driver.find_element(By.ID,"submit").click()
    success_text = driver.find_element(By.XPATH,"//p[text()='Congratulations! Your order has been confirmed!']").text
    assert "Congratulations! Your order has been confirmed!" in success_text
    