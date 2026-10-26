from modules import *
from page_object_model import test_cases_page

data_file= r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\test_case_page_url.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]


@pytest.mark.test_case_page
@pytest.mark.parametrize("data",data_data)
def test_contact_us(browser_fixture,data):
    driver = browser_fixture
    test_case = test_cases_page
    test_case.test_case_page(driver,data["url"])