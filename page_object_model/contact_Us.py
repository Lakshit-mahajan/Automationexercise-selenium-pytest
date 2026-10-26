from modules import *


def contactus(driver,url,name,email,subject,message,file):
    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//div[@class='features_items']/h2").text
    assert "FEATURES ITEMS" in home_page_text

    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//div//ul//li[8]/a").click()

    contact_page_text = driver.find_element(By.XPATH,"//div[@class='contact-form']//h2").text
    assert "GET IN TOUCH" in contact_page_text

    driver.find_element(By.NAME,"name").send_keys(name)
    driver.find_element(By.NAME,"email").send_keys(email)
    driver.find_element(By.NAME,"subject").send_keys(subject)
    driver.find_element(By.NAME,"message").send_keys(message)
    file_upload = driver.find_element(By.NAME,"upload_file")
    file_upload.send_keys(file)
    driver.find_element(By.NAME,"submit").click()

    handle_alert = driver.switch_to.alert
    handle_alert.accept()
    wait = WebDriverWait(driver,4)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@style='display: block;']")))
    success_text = driver.find_element(By.XPATH,"//div[@style='display: block;']").text
    assert "Success! Your details have been submitted successfully." in success_text

    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[1]/a").click()
    assert driver.current_url in url