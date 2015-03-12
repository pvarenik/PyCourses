__author__ = 'pvarenik'


def test_del_first_contact(app):
    app.session.login(username="Admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()