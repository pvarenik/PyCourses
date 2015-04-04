__author__ = 'pvarenik'
import re


def test_data_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_home(contact_from_edit_page)
    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_mails_from_home_page == merge_mails_like_home(contact_from_edit_page)

def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_home(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.homephone, contact.mobilephone, contact.workphone]))))

def merge_mails_like_home(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                    [contact.mail, contact.mail2, contact.mail3])))