from modules import *
from page_object_model import View_category_products


data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\Login_correct_credentials.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]


@pytest.mark.view_category_products
@pytest.mark.parametrize("data",data_data)

def test_view_category_product(browser_fixture,data):
    driver = browser_fixture
    test_view_category_product_ = View_category_products
    test_view_category_product_.view_category_products(driver,data["url"])