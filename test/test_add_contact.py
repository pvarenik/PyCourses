# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


def test_add_contact(app, db, json_contacts, check_ui):
    with pytest.allure.step("Get contacts"):
        contact = json_contacts
        old_contacts = db.get_contact_list()
    with pytest.allure.step("Create contact"):
        app.contact.create(contact)
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
    with pytest.allure.step("Verificate that contact was added"):
        if check_ui:
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)