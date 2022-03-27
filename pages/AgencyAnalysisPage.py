from pages.BasePage import BasePage


class AgentAnalysisPage(BasePage):
    """
    class contains xpath for required elements of Agent analysis Page.
    """
    SELECT_AGENCY = "//select//following-sibling::a[text()='Select Agency']"
    SELECT_AGENCY_OPTIONS = "//div[@class ='multiselect-options']//ul//span"
    SELECT_AGENCY_DONE = "//a[text()='Done']"
    COST_VARIANCE = "//ul[@class ='analysis']//a[text()='Cost Variance']"
    COST_VARIANCE_SOURCE_DATA = "//div[@class ='download'] // a[text()='Cost Variance Source Data']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_select_agency_dropdown(self):
        """function will click on select agency dropdown"""
        self.do_click(self.SELECT_AGENCY)

    def select_agencies(self, values):
        """function will select multiple agencies from dropdown"""
        self.select_multiple_value_from_dropdown(self.SELECT_AGENCY_OPTIONS, values)
        self.do_click(self.SELECT_AGENCY_DONE)

    def click_cost_variance(self):
        """function will click on cost variance button"""
        self.do_click(self.COST_VARIANCE)

    def mouse_over_download_button(self):
        """function will mouse over on download file link"""
        self.mouse_over_element(self.COST_VARIANCE_SOURCE_DATA)

    def click_download_cost_variance_source_data(self):
        """function will click on download cost variance sour data link"""
        self.do_click(self.COST_VARIANCE_SOURCE_DATA)
