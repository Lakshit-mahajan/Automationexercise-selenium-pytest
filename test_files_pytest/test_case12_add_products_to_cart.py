from modules import *
from page_object_model import addProducts_in_cart


data_file= r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\contact_us.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]


@pytest.mark.add_products_to_cart
@pytest.mark.parametrize("data",data_data)
def test_add_products_to_cart(browser_fixture,data):
    driver = browser_fixture
    test_add_products_to_cart_ = addProducts_in_cart
    test_add_products_to_cart_.add_products_to_cart(driver,data["url"],data["product_list"],data["expected_product1"],data["expected_product2"])