from modules import *
from page_object_model import product_page_verify



data_file= r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\test_case_page_url.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]

@pytest.mark.verify_product_page
@pytest.mark.parametrize("data",data_data)
def test_product_page_details(browser_fixture,data):
    driver = browser_fixture
    test_product_page = product_page_verify
    test_product_page.verify_product_page_and_details(driver,data["url"])