import datetime
import time

import pytest

from config.Configurations import Configurations
from pages.AgencyAnalysisPage import AgentAnalysisPage
from pages.HomePage import HomePage


@pytest.mark.usefixtures('init_browser')
class TestBlvSolutionPythonChallenge:
    def test_python_challenge(self):
        """
        This test function will verify RPA Python Challenge.
        """
        home_page = HomePage(self.driver)
        assert home_page.get_current_page_title() == Configurations.HOME_PAGE_TITLE,\
            "Not able to open Home pages."
        home_page.click_agency_analysis()
        agency_analysis_page = AgentAnalysisPage(self.driver)
        assert Configurations.AGENCY_ANALYSIS_PAGE_TITLE == \
               agency_analysis_page.get_current_page_title(),\
            "Not able to open agency analysis pages."
        if Configurations.AGENCY_LIST:
            agency_analysis_page.click_select_agency_dropdown()
            agency_analysis_page.select_agencies(Configurations.AGENCY_LIST)
            agency_analysis_page.click_cost_variance()
            agency_analysis_page.mouse_over_download_button()
            agency_analysis_page.take_screen_shot(
                "cost_variance_"+datetime.datetime.now().strftime(
                    "%Y_%m_%d_%H_%M_%S")+".png")
            agency_analysis_page.click_download_cost_variance_source_data()
            time.sleep(20)




