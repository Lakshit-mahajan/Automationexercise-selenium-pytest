from modules import *
from page_object_model import Add_review_on_product


data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\Add_review_on_product.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]

@pytest.mark.add_review_on_product
@pytest.mark.parametrize("data",data_data)
def test_add_review_on_product(browser_fixture,data):
    driver = browser_fixture
    test_add_review_on_product_ = Add_review_on_product
    test_add_review_on_product_.Add_review_on_product(driver,data["url"],data["name"],data["email"],data["review"])