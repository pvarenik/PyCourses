__author__ = 'pvarenik'
import re
from model.contact import Contact

def test_data_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contact_from_home_page) == len(contacts_from_db)
    for i in range(len(contacts_from_db)):
        assert contact_from_home_page[i].all_phones_from_home_page == merge_phones_like_home(contacts_from_db[i])
        assert contact_from_home_page[i].name == contacts_from_db[i].name
        assert contact_from_home_page[i].lastname == contacts_from_db[i].lastname
        assert contact_from_home_page[i].address == contacts_from_db[i].address.replace("\r\n", "\n")
        assert contact_from_home_page[i].all_mails_from_home_page == merge_mails_like_home(contacts_from_db[i])



def test_data_on_edit_page(app, db):
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contact_from_edit_page = sorted(app.contact.get_contacts_info_from_edit_page(), key=Contact.id_or_max)
    assert len(contact_from_edit_page) == len(contacts_from_db)
    for i in range(len(contacts_from_db)):
        assert contacts_from_db[i].name == contact_from_edit_page[i].name
        assert contacts_from_db[i].lastname == contact_from_edit_page[i].lastname
        assert contacts_from_db[i].address.replace("\r\n", "\n") == contact_from_edit_page[i].address
        assert contacts_from_db[i].mail == contact_from_edit_page[i].mail
        assert contacts_from_db[i].mail2 == contact_from_edit_page[i].mail2
        assert contacts_from_db[i].mail3 == contact_from_edit_page[i].mail3
        assert contacts_from_db[i].homephone == contacts_from_db[i].homephone
        assert contacts_from_db[i].workphone == contacts_from_db[i].workphone
        assert contacts_from_db[i].mobilephone == contacts_from_db[i].mobilephone

def test_phones_on_view_page(app, db):
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_view = sorted(app.contact.get_contacts_info_from_view_page(), key=Contact.id_or_max)
    assert len(contacts_from_view) == len(contacts_from_db)
    for i in range(len(contacts_from_db)):
        assert contacts_from_view[i].homephone == contacts_from_db[i].homephone
        assert contacts_from_view[i].workphone == contacts_from_db[i].workphone
        assert contacts_from_view[i].mobilephone == contacts_from_db[i].mobilephone

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_home(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.homephone, contact.mobilephone, contact.workphone, contact.secondary]))))

def merge_mails_like_home(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                    [contact.mail, contact.mail2, contact.mail3])))