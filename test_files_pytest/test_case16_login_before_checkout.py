from modules import *
from page_object_model import login_before_checkout


data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\register_before_checkout.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]

@pytest.mark.login_before_checkout
@pytest.mark.parametrize("data",data_data)
def test_login_before_checkout(browser_fixture,data):

    driver = browser_fixture
    test_login_before_checkout_ = login_before_checkout
    test_login_before_checkout_.login_before_checkout(driver,data["url"],data["name"],data["email"],data["password"],data["address"],data["comment"],data["name_on_card"],data["card_number"],data["cvc"],data["e"],data["year"])
