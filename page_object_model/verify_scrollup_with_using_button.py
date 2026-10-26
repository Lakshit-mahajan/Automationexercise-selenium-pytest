from modules import *


def verify_scroll_up_with_using_button(driver,url):
    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//h2[text()='Features Items']").text
    assert "FEATURES ITEMS" in home_page_text

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    wait = WebDriverWait(driver,10)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='single-widget']/h2")))
    subscription_text = driver.find_element(By.XPATH,"//div[@class='single-widget']/h2").text
    assert "SUBSCRIPTION" in subscription_text
    driver.find_element(By.ID,"scrollUp").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='item active']/div/h2")))

