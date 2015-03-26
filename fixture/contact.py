__author__ = 'pvarenik'
from model.contact import Contact

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
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.go_to_contacts()
        #select
        wd.find_element_by_name("selected[]").click()
        #delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.go_to_contacts()
        self.contact_cache = None

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
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.go_to_contacts()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_contacts()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                text = element.text
                if text != '':
                    _name = text.split(" ")[1]
                    _lastneme = text.split(" ")[0]
                else:
                    _name = ""
                    _lastneme = ""
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(name=_name, lastname=_lastneme, id=id))
        return list(self.contact_cache)