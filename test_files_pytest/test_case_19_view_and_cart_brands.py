from modules import *
from page_object_model import view_and_cart_brands

data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\view_and_cart_brand_products.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]

@pytest.mark.view_and_cart_brands
@pytest.mark.parametrize("data",data_data)
def test_view_and_cart_brands(browser_fixture,data):
    driver = browser_fixture
    view_and_cart_brands_ = view_and_cart_brands
    view_and_cart_brands_.view_and_cart_products(driver,data["url"])

