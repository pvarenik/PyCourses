__author__ = 'pvarenik'
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("first", "middle", "last", "nick"))
    app.contact.edit(Contact("first_edit", "middle_edit", "last_edit", "nick_edit"))