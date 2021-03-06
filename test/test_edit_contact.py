__author__ = 'pvarenik'
from model.contact import Contact
import random
import pytest


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("first", "middle", "last", "nick"))
    with pytest.allure.step("Getting contacts from DB"):
        old_contacts = db.get_contact_list()
    contact = Contact("first_edit_555555555555555", "middle_edit", "last_edit", "nick_edit")
    contact_to_edit = random.choice(old_contacts)
    index = old_contacts.index(contact_to_edit)
    contact.id = old_contacts[index].id
    with pytest.allure.step("Edit contact"):
        app.contact.edit(contact)
    with pytest.allure.step("Getting new contacts from DB"):
        new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    with pytest.allure.step("Verify that contacts was deleted"):
        if check_ui:
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

