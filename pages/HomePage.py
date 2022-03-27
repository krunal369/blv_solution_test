from pages.BasePage import BasePage


class HomePage(BasePage):
    """
    class contains xpath for required elements of Agent analysis Page.
    """
    AGENCY_ANALYSIS_IN_IT_COST_TRANSPARENCY =\
        "//h2[text()='IT Cost Transparency']/parent::div//ul//li//a[@href='/agency-analysis']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_agency_analysis(self):
        """ click on agency analysis under the “IT Cost Transparency” container"""
        self.do_click(self.AGENCY_ANALYSIS_IN_IT_COST_TRANSPARENCY)

