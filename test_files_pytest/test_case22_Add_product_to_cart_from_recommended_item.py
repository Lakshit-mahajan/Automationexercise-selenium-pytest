from modules import *
from page_object_model import Add_product_to_cart_from_recommended_item

data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\Add_review_on_product.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]


@pytest.mark.Add_product_to_cart_from_recommended_item
@pytest.mark.parametrize("data",data_data)
def test_Add_product_to_cart_from_recommended_item(browser_fixture,data):
    driver = browser_fixture
    test_Add_product_to_cart_from_recommended_item_ = Add_product_to_cart_from_recommended_item
    test_Add_product_to_cart_from_recommended_item_.Add_product_to_cart_from_recommended_item(driver,data["url"])
    
