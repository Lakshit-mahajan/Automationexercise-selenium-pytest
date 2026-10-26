from modules import *


def test_case_page(driver,url):
    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//div[@class='features_items']/h2").text
    assert "FEATURES ITEMS" in home_page_text

    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[5]/a").click()
    wait = WebDriverWait(driver,4)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@style='color: red;']")))
    test_case_page_text = driver.find_element(By.XPATH,"//span[@style='color: red;']").text
    assert "Click on the scenario for detailed Test Steps:" in test_case_page_text