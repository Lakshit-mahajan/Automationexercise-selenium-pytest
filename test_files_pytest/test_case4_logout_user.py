from modules import *
from page_object_model import logout_user


data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\Login_correct_credentials.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]

@pytest.mark.logout_user
@pytest.mark.parametrize("data",data_data)

def test_logout_user(browser_fixture,data):
    driver = browser_fixture
    test_logoutuser= logout_user
    test_logoutuser.Logout_user(driver,data["url"],data["email"],data["password"],data["name"])
