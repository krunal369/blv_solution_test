from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
    Class is used common function related to driver reference.
    """
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_visible(self, by_locator):
        """function will wait for visibility of element"""
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, by_locator)))

    def get_element(self, by_locator):
        """function will find element from web page"""
        element = self.wait_for_element_to_visible(by_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def do_click(self, by_locator):
        """function will click on button/link"""
        self.driver.execute_script("arguments[0].click();", self.get_element(by_locator))

    def select_multiple_value_from_dropdown(self, by_locator, values_to_select):
        """function will select multiple option from dropdown"""
        dropdown_list_options = self.driver.find_elements(By.XPATH, by_locator)
        for dropdown_option in dropdown_list_options:
            if dropdown_option.text in values_to_select:
                dropdown_option.click()

    def mouse_over_element(self, by_locator):
        """function will mouse over at any element on webpage"""
        ActionChains(self.driver).move_to_element(self.get_element(by_locator)).perform()

    def take_screen_shot(self, file_name):
        """function will take a screenshot of web page"""
        self.driver.get_screenshot_as_file(file_name)

    def get_current_page_title(self):
        """function will return title of current web page."""
        return self.driver.title
