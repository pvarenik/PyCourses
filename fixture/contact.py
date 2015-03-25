__author__ = 'pvarenik'


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.get("http://localhost/addressbook/")

    def delete_first_contact(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        #select
        wd.find_element_by_name("selected[]").click()
        #delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.get("http://localhost/addressbook/")

    def edit(self, contact):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("update").click()
        wd.get("http://localhost/addressbook/")

    def count(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        return len(wd.find_elements_by_name("selected[]"))