from modules import *


def register_before_checkout(driver,url,name,email,password,day,month,year,first_name,last_name,company,address,address2,country,state,city,zipcode,mobile,comment,name_on_card,card_number,cvc,e):
    driver.implicitly_wait(5)
    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//h2[text()='Features Items']").text
    assert "FEATURES ITEMS" in home_page_text

    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[4]/a").click()
    driver.find_element(By.NAME,"name").send_keys(name)
    driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys(email)
    driver.find_element(By.XPATH,"//button[@data-qa='signup-button']").click()
    driver.find_element(By.ID,"id_gender1").click()
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"days").send_keys(day)
    driver.find_element(By.ID,"months").send_keys(month)
    driver.find_element(By.ID,"years").send_keys(year)
    driver.find_element(By.ID,"newsletter").click()
    driver.find_element(By.ID,"optin").click()
    driver.find_element(By.ID,"first_name").send_keys(first_name)
    driver.find_element(By.ID,"last_name").send_keys(last_name)
    driver.find_element(By.ID,"company").send_keys(company)
    driver.find_element(By.ID,"address1").send_keys(address)
    driver.find_element(By.ID,"address2").send_keys(address2)
    country_select = Select(driver.find_element(By.ID,"country"))
    country_select.select_by_value(country)
    driver.find_element(By.ID,"state").send_keys(state)
    driver.find_element(By.ID,"city").send_keys(city)
    driver.find_element(By.ID,"zipcode").send_keys(zipcode)
    driver.find_element(By.ID,"mobile_number").send_keys(mobile)
    driver.find_element(By.XPATH,"//button[text()='Create Account']").click()
    driver.find_element(By.XPATH,"//a[text()='Continue']").click()

    login_text = driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[10]/a").text
    assert name in login_text

    driver.find_element(By.XPATH,"//a[@data-product-id='4']").click()
    driver.find_element(By.XPATH,"//a[@href='/view_cart']/u").click()

    cart_page_url = driver.current_url
    assert "/view_cart" in cart_page_url
    driver.find_element(By.XPATH,"//a[text()='Proceed To Checkout']").click()
    address_1 = driver.find_element(By.XPATH,"//ul[@id='address_delivery']//li[4]").text
    assert address in  address_1
    

    driver.find_element(By.XPATH,"//a[text()='Place Order']").click()
    driver.find_element(By.NAME,"name_on_card").send_keys(name_on_card)
    driver.find_element(By.NAME,"card_number").send_keys(card_number)
    driver.find_element(By.NAME,"cvc").send_keys(cvc)
    driver.find_element(By.NAME,"expiry_month").send_keys(year)
    driver.find_element(By.NAME,"expiry_year").send_keys(2090)
    driver.find_element(By.ID,"submit").click()
    success_text = driver.find_element(By.XPATH,"//p[text()='Congratulations! Your order has been confirmed!']").text
    assert "Congratulations! Your order has been confirmed!" in success_text

    