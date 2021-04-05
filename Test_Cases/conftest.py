import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="my option: type1 or type2")


@pytest.fixture(scope="class")
def setup(request):
    browserName = request.config.getoption("browser_name")

    if browserName == "chrome":
        option = Options()
        prefs = {"profile.default_content_setting_values.notifications": 1}
        option.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=option, executable_path="D:\Drivers\chromedriver.exe")
        driver.get("https://mla-test.azurewebsites.net/Default.aspx?")
        driver.maximize_window()

    elif browserName == "fireFox":
        driver = webdriver.Chrome(executable_path="D:\Local Disk\Asad\Drivers\geckodriver.exe")
        driver.get("https://staging-encore.brandedonline.com/Login")
        driver.maximize_window()

    elif browserName == "ie":
        # IE invocation
        pass
    request.cls.driver = driver
    yield
    # driver.close()
    driver.quit()
