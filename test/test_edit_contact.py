__author__ = 'pvarenik'
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit(Contact("first_edit", "middle_edit", "last_edit", "nick_edit"))