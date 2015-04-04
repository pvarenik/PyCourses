__author__ = 'pvarenik'
from model.contact import Contact
import re

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

    def select_contact_by_id(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_id(self, index):
        wd = self.app.wd
        self.go_to_contacts()
        #select
        self.select_contact_by_id(index)
        #delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.go_to_contacts()
        self.contact_cache = None

    def edit(self, contact, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("update").click()
        self.go_to_contacts()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_to_contacts()
        self.select_contact_by_id(index)
        wd.find_elements_by_css_selector("tr[name=entry]")[index].find_element_by_css_selector("img[title=Edit]").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.go_to_contacts()
        self.select_contact_by_id(index)
        wd.find_elements_by_css_selector("tr[name=entry]")[index].find_element_by_css_selector("img[title=Details]").click()

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
                cells = element.find_elements_by_tag_name("td")
                name = cells[2].text
                lastneme = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_mails_from_home_page = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(name=name, lastname=lastneme, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_mails_from_home_page=all_mails_from_home_page,
                                                  address=address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        mail = wd.find_element_by_name("email").get_attribute("value")
        mail2 = wd.find_element_by_name("email2").get_attribute("value")
        mail3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(name=name, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                       mail=mail, mail2=mail2, mail3=mail3, address=address)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone)
