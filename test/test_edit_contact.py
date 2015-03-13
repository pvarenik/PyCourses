__author__ = 'pvarenik'
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="Admin", password="secret")
    app.contact.edit(Contact("first_edit", "middle_edit", "last_edit", "nick_edit"))
    app.session.logout()