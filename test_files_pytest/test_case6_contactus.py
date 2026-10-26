from modules import *
from page_object_model import contact_Us

data_file= r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\contact_us.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]

@pytest.mark.contact_us
@pytest.mark.parametrize("data",data_data)
def test_contact_us(browser_fixture,data):
    driver = browser_fixture
    test_contactpage = contact_Us
    test_contactpage.contactus(driver,data["url"],data["name"],data["email"],data["subject"],data["message"],data["file"])
