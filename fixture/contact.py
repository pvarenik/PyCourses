__author__ = 'pvarenik'


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def go_to_contacts(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("new"))):
            wd.get("http://localhost/addressbook/")

    def create(self, contact):
        wd = self.app.wd
        self.go_to_contacts()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.go_to_contacts()

    def delete_first_contact(self):
        wd = self.app.wd
        self.go_to_contacts()
        #select
        wd.find_element_by_name("selected[]").click()
        #delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.go_to_contacts()

    def edit(self, contact):
        wd = self.app.wd
        self.go_to_contacts()
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("update").click()
        self.go_to_contacts()

    def count(self):
        wd = self.app.wd
        self.go_to_contacts()
        return len(wd.find_elements_by_name("selected[]"))