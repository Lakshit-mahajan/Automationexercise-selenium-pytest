from modules import *

def verify_address_details_in_checkout_page(driver,
                  url,
                  name,
                  email,
                  title,
                  password,
                  day,
                  month,
                  year,
                  first_name,
                  last_name,
                  company,
                  address,
                  address2,
                  country,
                  state,
                  city,zipcode,
                  mobile):

    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//div[@class='features_items']/h2").text
    assert "FEATURES ITEMS" in home_page_text

    driver.find_element(By.XPATH,"//div[@class='col-sm-8']/div/ul/li[4]/a").click()

    signup_page_text = driver.find_element(By.XPATH,"//div[@class='signup-form']/h2").text
    assert "New User Signup!" in signup_page_text

    driver.find_element(By.XPATH,"//form[@action='/signup']//input[2]").send_keys(name)
    driver.find_element(By.XPATH,"//form[@action='/signup']//input[3]").send_keys(email)
    driver.find_element(By.XPATH,"//button[text()='Signup']").click()

    signup_page2_text = driver.find_element(By.XPATH,"//b[text()='Enter Account Information']").text
    assert "ENTER ACCOUNT INFORMATION" in signup_page2_text


    driver.find_element(By.XPATH,f"//input[@value='{title}']").click()
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

    countries = Select(driver.find_element(By.ID,"country"))
    countries.select_by_value(country)
    driver.find_element(By.ID,"state").send_keys(state)
    driver.find_element(By.ID,"city").send_keys(city)
    driver.find_element(By.ID,"zipcode").send_keys(zipcode)
    driver.find_element(By.ID,"mobile_number").send_keys(mobile)
    driver.find_element(By.XPATH,"//button[@data-qa='create-account']").click()

    wait = WebDriverWait(driver,5)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//b[text()='Account Created!']")))
    account_created_text = driver.find_element(By.XPATH,"//b[text()='Account Created!']").text
    assert "ACCOUNT CREATED" in account_created_text

    driver.find_element(By.XPATH,"//a[text()='Continue']").click()

    logged_in_text = driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[10]//a").text

    assert f"Logged in as {name}" in logged_in_text

    driver.execute_script("window.scrollBy(700,700);")

    driver.find_element(By.XPATH,"//a[@data-product-id='1']").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//u[text()='View Cart']")))
    driver.find_element(By.XPATH,"//u[text()='View Cart']").click()

    cart_url = driver.current_url
    print(cart_url)
    driver.find_element(By.XPATH,"//a[text()='Proceed To Checkout']").click()

    address_1 = driver.find_element(By.XPATH,"//ul[@id='address_delivery']/li[4]").text
    address_2 = driver.find_element(By.XPATH,"//ul[@id='address_delivery']/li[5]").text
    assert address == address_1
    assert address2 == address_2

    billing_address_1 = driver.find_element(By.XPATH,"//ul[@id='address_invoice']/li[4]").text
    billing_address_2 = driver.find_element(By.XPATH,"//ul[@id='address_invoice']/li[5]").text
    assert address == billing_address_1
    assert address2 == billing_address_2