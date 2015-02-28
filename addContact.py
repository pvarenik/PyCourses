# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class addContact(unittest.TestCase):
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

    def createAccount(self, wd, contact):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_addContact(self):
        wd = self.wd
        self.open(wd)
        self.login(wd, username="Admin", password="secret")
        self.createAccount(wd, Contact("test contact"))
        self.logout(wd)

    def test_empty_addContact(self):
        wd = self.wd
        self.open(wd)
        self.login(wd, username="Admin", password="secret")
        self.createAccount(wd, Contact(""))
        self.logout(wd)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
