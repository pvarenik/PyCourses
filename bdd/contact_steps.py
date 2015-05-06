__author__ = 'pvarenik'

from pytest_bdd import given, when, then
from model.contact import Contact
import random
import pytest

@pytest.allure.step("a contact list")
@given("a contact list")
def contact_list(db):
    return db.get_contact_list()

@pytest.allure.step("a contact with first={first}, middle={middle}, last={last} and nick={nick}")
@given("a contact with <first>, <middle>, <last> and <nick>")
def new_contact(first, middle, last, nick):
    return Contact(name=first, middlename=middle, lastname=last, nickname=nick)

@when("I add the new contact to the list")
def add_new_contact(app, new_contact):
    with pytest.allure.step("When I add the new contact %s to the list"):
        app.contact.create(new_contact)

@then("the new contact list is equal to the old list with the added contact")
def verify_contact_added(db, contact_list, new_contact):
    with pytest.allure.step("Then the new contact list is equal to the old list with the added contact"):
        old_contacts = contact_list
        new_contacts = db.get_contact_list()
        old_contacts.append(new_contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@pytest.allure.step("a non-empty contact list")
@given("a non-empty contact list")
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="name"))
    return db.get_contact_list()

@pytest.allure.step("a random contact from the list")
@given("a random contact from the list")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when("I delete the contact from the list")
def delete_contact(app, random_contact):
    with pytest.allure.step("When I delete the contact from the list"):
        app.contact.delete_contact_by_id(random_contact.id)

@then("the new contact list is equal to the old list without the deleted contact")
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    with pytest.allure.step("Then the new contact list is equal to the old list without the deleted contact"):
        old_contacts = non_empty_contact_list
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == app.contact.count()
        old_contacts.remove(random_contact)
        assert old_contacts == new_contacts
    with pytest.allure.step("Also check UI"):
        if check_ui:
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@pytest.allure.step("a contact with name={name}, middlename={middlename}, lastname={nickname}, nick={nickname}")
@given("a contact with <name>, <middlename>, <lastname>, <nickname>")
def random_contact_edited(non_empty_contact_list, random_contact, name, middlename, lastname, nickname):
    index = non_empty_contact_list.index(random_contact)
    contact = Contact(name=name, middlename=middlename, lastname=lastname, nickname=nickname)
    contact.id = non_empty_contact_list[index].id
    return {"old":non_empty_contact_list[index], "new":contact}

@when("I edit the contact from the list")
def edit_contact(app, random_contact_edited):
    #contact = Contact(name="bdd_contact", middlename="middle_edit", lastname="last_edit", nickname="nick_edit")
    with pytest.allure.step("When I edit the contact from the list"):
        app.contact.edit(random_contact_edited["new"])


@then("the new contact list is equal to the old list with the edited contact")
def verify_contact_edited(db, non_empty_contact_list, random_contact_edited):
    with pytest.allure.step("Then the new contact list is equal to the old list with the edited contact"):
        old_contacts = non_empty_contact_list
        new_contacts = db.get_contact_list()
        old_contacts[non_empty_contact_list.index(random_contact_edited["old"])] = random_contact_edited["new"]
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)