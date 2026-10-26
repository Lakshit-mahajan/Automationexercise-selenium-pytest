
from modules import *
from page_object_model import verify_subscription

data_file= r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\contact_us.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]


@pytest.mark.verify_subscription
@pytest.mark.parametrize("data",data_data)
def test_verify_subscription(browser_fixture,data):
    driver = browser_fixture
    test_verify_subscription_pytest = verify_subscription
    test_verify_subscription_pytest.verify_subscription_home_page(driver,data["url"],data["email"])