__author__ = 'pvarenik'
from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("first", "middle", "last", "nick"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact("first_edit", "middle_edit", "last_edit", "nick_edit")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

