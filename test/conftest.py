import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.Configurations import Configurations


@pytest.fixture(params=["chrome"], scope="class")
def init_browser(request):
    """
    Fixture is used initialize the browser in headless mode.
    """
    current_file_path = os.path.dirname(__file__)
    last_index = current_file_path.rfind("\\")
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": current_file_path[0:last_index+1],
                 "directory_upgrade": True}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu");
        driver = webdriver.Chrome(options=chrome_options
                                  , service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(Configurations.IMPLICIT_WAIT)
        driver.set_window_size(1920, 1080)
        driver.get(Configurations.BASE_URL)
        request.cls.driver = driver
        yield
        driver.close()
