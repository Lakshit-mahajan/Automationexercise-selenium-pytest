from modules import *
from page_object_model import download_invoice


def download_invoice(driver,url,
                            name,
                            email,
                            password,
                            day,
                            month,
                            year,
                            firstname,
                            lastname,
                            company,
                            address,
                            address2,
                            country,
                            state,
                            city,
                            zipcode,
                            mobile,
                            name_on_card,
                            card_number,
                            cvc,
                            e,
                            yyyy,
                            comment):

    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//h2[text()='Features Items']").text
    assert "FEATURES ITEMS" in home_page_text
    driver.execute_script("window.scrollBy(500,500);")


    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH,"//div[@class='col-sm-4']/div/div//a")).click().perform()
    time.sleep(4)
    driver.find_element(By.XPATH,"//div[@class='modal-body']/p[2]/a/u").click()
    current_url = driver.current_url
    assert "/view_cart" in current_url
    driver.find_element(By.XPATH,"//a[text()='Proceed To Checkout']").click()
    driver.find_element(By.XPATH,"//p[@class='text-center']/a/u").click()

    signup_page_text = driver.find_element(By.XPATH,"//div[@class='signup-form']/h2").text
    assert "New User Signup!" in signup_page_text
    
    driver.find_element(By.XPATH,"//form[@action='/signup']//input[2]").send_keys(name)        
    driver.find_element(By.XPATH,"//form[@action='/signup']//input[3]").send_keys(email)
    driver.find_element(By.XPATH,"//button[text()='Signup']").click()
    
    signup_page2_text = driver.find_element(By.XPATH,"//b[text()='Enter Account Information']").text
    assert "ENTER ACCOUNT INFORMATION" in signup_page2_text
    
    
    # driver.find_element(By.XPATH,f"//input[@value='{title}']").click()
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"days").send_keys(day)
    driver.find_element(By.ID,"months").send_keys(month)
    driver.find_element(By.ID,"years").send_keys(year)
    driver.find_element(By.ID,"newsletter").click()
    driver.find_element(By.ID,"optin").click()
    driver.find_element(By.ID,"first_name").send_keys(firstname)
    driver.find_element(By.ID,"last_name").send_keys(lastname)
    driver.find_element(By.ID,"company").send_keys(company)
        
    driver.find_element(By.ID,"address1").send_keys(address)
    driver.find_element(By.ID,"address2").send_keys(address2)
    
    countries = Select(driver.find_element(By.ID,"country"))
    countries.select_by_value(country)
    driver.find_element(By.ID,"state").send_keys(state)
    driver.find_element(By.ID,"city").send_keys(city)
    driver.find_element(By.ID,"zipcode").send_keys(zipcode)
    driver.find_element(By.ID,"mobile_number").send_keys(mobile)
    driver.find_element(By.XPATH,"//button[@data-qa='create-account']").click()
    time.sleep(4)
    created_text = driver.find_element(By.XPATH,"//b[text()='Account Created!']").text
    assert "ACCOUNT CREATED" in created_text
    driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()
    time.sleep(4)

    loggin_text = driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[10]/a").text
    print(loggin_text)
    assert name in loggin_text
    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[3]/a").click()
    driver.find_element(By.XPATH,"//a[text()='Proceed To Checkout']").click()

    address_ = driver.find_element(By.XPATH,"//ul[@id='address_delivery']//li[4]").text
    assert "address1_lelelelele" in address_
    driver.find_element(By.NAME,"message").send_keys(comment)
    driver.find_element(By.XPATH,"//a[text()='Place Order']").click()
    driver.find_element(By.NAME,"name_on_card").send_keys(name_on_card)
    driver.find_element(By.NAME,"card_number").send_keys(card_number)
    driver.find_element(By.NAME,"cvc").send_keys(cvc)
    driver.find_element(By.NAME,"expiry_month").send_keys(e)
    driver.find_element(By.NAME,"expiry_year").send_keys(yyyy)
    driver.find_element(By.ID,"submit").click()
    order_placed = driver.find_element(By.XPATH,"//p").text
    print(order_placed)
    assert "Congratulations! Your order has been confirmed!" in order_placed

    wait = WebDriverWait(driver,10)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//a[text()='Download Invoice']")))
    driver.find_element(By.XPATH,"//a[text()='Download Invoice']").click()
    time.sleep(4)

    file_read = r"C:\Users\ASUS\Downloads\invoice.txt"
    with open(file_read,"r") as read:
        first_line = read.readline()
        print(first_line)

    assert f"Hi {firstname} {lastname}, Your total purchase amount is" in first_line

    driver.find_element(By.XPATH,"//a[text()='Continue']").click()
    current_url2 = driver.current_url
    print(current_url2)