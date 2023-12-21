from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
# from data.urls import LINKEDIN_PAGE, GITHUB_PAGE, MAIN_PAGE, MAIN_PAGE_TEST
from data.urls import Urls


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, Urls.MAIN_PAGE_TEST)

    def logo_visibility(self):
        self.check_element_visibility(MainPageLocators.LOGO)

    def check_linkedin_redirection(self):
        self.find_element_and_click(MainPageLocators.LINKEDIN_LINK)
        self.switch_to_new_window()
        self.assert_current_url(Urls.LINKEDIN_PAGE)

    def check_github_redirection(self):
        self.find_element_and_click(MainPageLocators.GITHUB_LINK)
        self.assert_current_url(Urls.GITHUB_PAGE)
