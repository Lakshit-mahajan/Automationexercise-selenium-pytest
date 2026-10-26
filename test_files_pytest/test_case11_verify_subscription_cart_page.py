from modules import *
from page_object_model import verify_subscription_cart_page

data_file= r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\contact_us.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]


@pytest.mark.verify_subscription_cart_page
@pytest.mark.parametrize("data",data_data)

def test_verify_subscription_cart_page(browser_fixture,data):
    driver = browser_fixture
    test_verify_subscription_cart_page_ = verify_subscription_cart_page
    test_verify_subscription_cart_page_.verify_subsciption_cart_page(driver,data["url"],data["email"])
