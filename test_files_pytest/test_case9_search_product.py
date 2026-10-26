from modules import *
from page_object_model import search_product

data_file= r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\search_product.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]

@pytest.mark.search_product
@pytest.mark.parametrize("data",data_data)
def test_search_product(browser_fixture,data):
    driver = browser_fixture
    test_searchProduct = search_product
    test_searchProduct.search_product(driver,data["url"],data["product_name"])

