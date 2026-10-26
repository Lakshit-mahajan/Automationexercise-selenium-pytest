from modules import *
from page_object_model import verify_product_quantity


data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\verify_product_quantity.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]


@pytest.mark.verify_quantity
@pytest.mark.parametrize("data",data_data)

def test_verify_quantity(browser_fixture,data):
    driver = browser_fixture
    test_verify_quantity_ = verify_product_quantity
    test_verify_quantity_.verify_quantity_of_product(driver,data["url"],data["quantity"])
