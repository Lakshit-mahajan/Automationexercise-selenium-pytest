from modules import *
from page_object_model import Register_while_checkout


data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\Register_while_checkout.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]

@pytest.mark.register_while_checkout
@pytest.mark.parametrize("data",data_data)

def test_register_while_checkout(browser_fixture,data):
    driver = browser_fixture
    test_register_while_checkout_ = Register_while_checkout
    test_register_while_checkout_.register_while_checkout(driver,
                                                          data["url"],
                                                          data["name"],
                                                          data["email"],
                                                          data["password"],
                                                          data["day"],
                                                          data["month"],
                                                          data["year"],
                                                          data["firstname"],
                                                          data["lastname"],
                                                          data["company"],
                                                          data["address"],
                                                          data["address2"],
                                                          data["country"],
                                                          data["state"],
                                                          data["city"],
                                                          data["zipcode"],
                                                          data["mobile"],
                                                          data["name_on_card"],
                                                          data["card_number"],
                                                          data["cvc"],
                                                          data["ex"],
                                                          data["yyyy"],
                                                          data["comment"])
    