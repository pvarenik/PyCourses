from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
__author__ = 'pvarenik'

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # new group
        wd.find_element_by_name("new").click()
        # edit group fields
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # create group
        wd.find_element_by_name("submit").click()
        self.return_to_the_group_page()

    def create_account(self, contact):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_the_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()


    def destroy(self):
        self.wd.quit()