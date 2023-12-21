


class BasePage:

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link

    def open(self):
        self.driver.get(self.link)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def check_element_visibility(self, locator):
        element = self.find_element(locator)
        assert element.is_displayed()

    def check_element_clickability(self, locator):
        element = self.find_element(locator)
        assert element.is_enabled()

    def find_element_and_click(self, locator):
        self.find_element(locator).click()

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])


    def assert_current_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"URL does not match. Actual page is: {current_url}"
