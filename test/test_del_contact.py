__author__ = 'pvarenik'
from model.contact import Contact
import random


def test_del_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("first", "middle", "last", "nick"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    if check_ui:
        assert old_contacts == new_contacts