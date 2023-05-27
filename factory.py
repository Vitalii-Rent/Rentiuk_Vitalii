from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageFactory:
    def __init__(self):
        options = Options()
        driver = webdriver.Firefox(options=options)  # Change to the appropriate webdriver for your browser
        # Open the website
        driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver = driver

    def create_login_page(self):
        return LoginPage(self.driver)

    def create_admin_page(self):
        return AddAdminPage(self.driver)

    def create_titles_page(self):
        return AddTitlesPage(self.driver)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
        self.password_field = driver.find_element(By.NAME, "password")
        self.login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

    def enter_username(self, username):
        self.username_field.send_keys(username)

    def enter_password(self, password):
        self.password_field.send_keys(password)

    def click_login_btn(self):
        self.login_button.click()


class AddAdminPage:
    def __init__(self, driver):
        self.driver = driver

    def click_admin_btn(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//a[@class="oxd-main-menu-item" and contains(@href, "/admin/viewAdminModule")]'))).click()

    def click_job_btn(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//li[@class="oxd-topbar-body-nav-tab --parent" and contains(span/text(), "Job")]'))).click()

    def click_job_titles_btn(self):
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a').click()

    def click_add_btn(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button'))).click()

    def find_title_row(self, title):
        self.wait_titles_page()
        title_row = self.driver.find_elements(By.XPATH,
                                             f'//div[contains(text(), "{title}")]/ancestor::div[@class="oxd-table-card"]')
        return title_row

    def del_title(self, title_row):
        title_row[0].find_element(By.XPATH, './/i[@class="oxd-icon bi-trash"]/ancestor::button').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div/div[3]/button[2]').click()

    def wait_titles_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//div[@role="columnheader"]')))


class AddTitlesPage:
    def __init__(self, driver):
        self.title_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input')))
        self.description_field = driver.find_element(By.XPATH,
                                                     '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea')
        self.notes_filed = driver.find_element(By.XPATH,
                                               '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea')
        self.save_btn = driver.find_element(By.XPATH,
                                            "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]")

    def enter_title(self, title):
        self.title_field.send_keys(title)

    def enter_description(self, description):
        self.description_field.send_keys(description)

    def enter_notes(self, notes):
        self.notes_filed.send_keys(notes)

    def click_save_btn(self):
        self.save_btn.click()
