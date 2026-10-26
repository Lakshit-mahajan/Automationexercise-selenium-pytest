from modules import *
from page_object_model import verify_scroll_up_without_using_button

data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\Add_review_on_product.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]


@pytest.mark.verify_scroll_up_without_using_button
@pytest.mark.parametrize("data",data_data)

def test_verify_scrollup_without_using_button(browser_fixture,data):
    driver = browser_fixture
    test_verify_scrollup_without_using_button_ = verify_scroll_up_without_using_button
    test_verify_scrollup_without_using_button_.verify_scroll_up_without_using_button(driver,data["url"])
