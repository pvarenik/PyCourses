# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class addGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        wd.find_element_by_id("header").click()

    def openGroupsPage(self, wd):
        wd.find_element_by_link_text("groups").click()

    def createGroup(self, wd, group):
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

    def returnToTheGroupPage(self, wd):
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_addGroup(self):
        wd = self.wd
        self.open(wd)
        self.login(wd, username="Admin", password="secret")
        self.openGroupsPage(wd)
        self.createGroup(wd, Group(name="testgroup", header="New Group", footer="End of new group"))
        self.returnToTheGroupPage(wd)
        self.logout(wd)

    def test_empty_addGroup(self):
        wd = self.wd
        self.open(wd)
        self.login(wd, username="Admin", password="secret")
        self.openGroupsPage(wd)
        self.createGroup(wd, Group(name="", header="" , footer=""))
        self.returnToTheGroupPage(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
