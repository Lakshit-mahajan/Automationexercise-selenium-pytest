from modules import *
from page_object_model import Search_products_and_verify_after_login

data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\Search_products_and_verify_after_login.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]


@pytest.mark.search_product_and_verify_after_login
@pytest.mark.parametrize("data",data_data)
def test_search_product_and_verify_after_login(browser_fixture,data):
    driver = browser_fixture
    test_search_product_and_verify_after_login_ = Search_products_and_verify_after_login
    test_search_product_and_verify_after_login_.Search_products_and_verify_after_login(driver,data["url"],data["product_name"],data["email"],data["password"])