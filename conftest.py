from modules import *

driver  = None
def pytest_addoption(parser):
    # Add a custom command-line argument
    parser.addoption(
        "--browser", action="store", default="edge", help="browser"
    )

@pytest.fixture(scope="function")
def browser_fixture(request):
    browser = request.config.getoption("--browser")
    if browser == "edge":
        option = webdriver.EdgeOptions()
        option.add_argument("--start-maximized")
        option.add_argument("--headless")
        driver = webdriver.Edge(options=option)

    elif browser == "firefox":
        option = webdriver.FirefoxOptions()
        option.add_argument("--start-maximized")
        option.add_argument("--headless")
        driver = webdriver.Firefox(options=option)

    elif browser == "chrome":
        option = webdriver.ChromeOptions()
        option.add_argument("--start-maximized")
        # option.add_argument("--headless")
        driver = webdriver.Chrome(options=option)

    yield driver






@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):  
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    
    extras = getattr(report, 'extras', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            try:
                reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
                os.makedirs(reports_dir, exist_ok=True)
                
                clean_nodeid = report.nodeid.replace("::", "_").replace("[", "_").replace("]", "_").replace("/", "_").replace("\\", "_")
                file_name = os.path.join(reports_dir, f"{clean_nodeid}.png")
                print("test_.py file name is " + file_name)
                
                global driver
                if driver is not None:
                    _capture_screenshot(file_name)
                    
                    if os.path.exists(file_name) and pytest_html:
                        html_content = (
                            f'<div><img src="{file_name}" alt="screenshot" style="width:304px;height:228px;" '
                            f'onclick="window.open(this.src)" align="right"/></div>'
                        )
                        extras.append(pytest_html.extras.html(html_content))
                else:
                    print("Screenshot skipped: WebDriver context is None.")
                    
            except Exception as hook_err:
                print(f"Non-fatal error creating report visual assets: {hook_err}")
                
        report.extras = extras


def _capture_screenshot(file_name):
    try:
        if driver is not None:
            driver.get_screenshot_as_file(file_name)
    except Exception as e:
        print(f"Failed to write screenshot file to disk: {e}")
