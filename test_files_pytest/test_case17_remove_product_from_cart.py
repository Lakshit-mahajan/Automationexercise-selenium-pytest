from modules import *
from page_object_model import remove_product_from_cart


data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\Login_correct_credentials.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]


@pytest.mark.remove_product_from_cart
@pytest.mark.parametrize("data",data_data)

def test_remove_product_from_cart(browser_fixture,data):
    driver = browser_fixture
    test_remove_product_from_cart_ = remove_product_from_cart
    test_remove_product_from_cart_.remove_product_from_cart(driver,data["url"])

