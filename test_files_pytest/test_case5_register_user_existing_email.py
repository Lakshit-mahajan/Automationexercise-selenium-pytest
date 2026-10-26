from modules import *
from page_object_model import Register_user_existing_email



data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\register_user_exisiting_email.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]

@pytest.mark.register_user_existing_email
@pytest.mark.parametrize("data",data_data)

def test_register_user_existing_email(browser_fixture,data):
    driver = browser_fixture
    test_register_user_existing_email_ = Register_user_existing_email
    test_register_user_existing_email_.Register_user(driver,data["url"],data["name"],data["email"])