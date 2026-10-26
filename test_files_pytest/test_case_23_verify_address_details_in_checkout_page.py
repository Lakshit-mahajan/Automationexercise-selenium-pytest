from modules import *
from page_object_model import verify_address_details_in_checkout_page


data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\register_user_data.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]



@pytest.mark.verify_address_details_in_checkout_page
@pytest.mark.parametrize("data",data_data)
def test_verify_address_details_in_checkout_page(browser_fixture,data):
    driver = browser_fixture
    test_verify_address_details_in_checkout_page_ = verify_address_details_in_checkout_page
    test_verify_address_details_in_checkout_page_.verify_address_details_in_checkout_page(driver,
                                                     data["url"],
                                                     data["name"],
                                                     data["email"],
                                                     data["title"],
                                                     data["password"],
                                                     data["day"],
                                                     data["month"],
                                                     data["year"],
                                                     data["first_name"],
                                                     data["last_name"],
                                                     data["company"],
                                                     data["address"],
                                                     data["address2"],
                                                     data["country"],
                                                     data["state"],
                                                     data["city"],
                                                     data["zipcode"],
                                                     data["mobile"])