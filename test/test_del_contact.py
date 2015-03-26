__author__ = 'pvarenik'
from model.contact import Contact
from random import randrange


def test_del_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("first", "middle", "last", "nick"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_id(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts