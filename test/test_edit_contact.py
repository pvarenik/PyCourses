__author__ = 'pvarenik'
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("first", "middle", "last", "nick"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact("first_edit", "middle_edit", "last_edit", "nick_edit")
    contact.id = old_contacts[0].id
    app.contact.edit(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

