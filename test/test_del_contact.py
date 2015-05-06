__author__ = 'pvarenik'
from model.contact import Contact
import random
import pytest


def test_del_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("first", "middle", "last", "nick"))
    with pytest.allure.step("Getting contacts from DB"):
        old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    with pytest.allure.step("Delete contact with %s id" % contact.id):
        app.contact.delete_contact_by_id(contact.id)
    with pytest.allure.step("Getting new contacts from DB"):
        new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    with pytest.allure.step("Verify that contact was deleted"):
        if check_ui:
            assert old_contacts == new_contacts