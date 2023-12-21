from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO = (By.CSS_SELECTOR, 'img[alt="Logo"]')
    LINKEDIN_LINK = (By.CSS_SELECTOR, "[alt='linkedin']")
    GITHUB_LINK = (By.CSS_SELECTOR, "[alt='github']")
    ABOUT_US_BUTTON = (By.CSS_SELECTOR, '[class="Navigation_link__Jlf0e active"]:first-of-type')
    TASKS_BUTTON = (By.CSS_SELECTOR, '[class="Navigation_link__Jlf0e active"]:nth-of-type(2)')
    REG_BUTTON = (By.CSS_SELECTOR, "[href='/auth']")
    HEADER_BUTTONS = [ABOUT_US_BUTTON, TASKS_BUTTON, REG_BUTTON]
