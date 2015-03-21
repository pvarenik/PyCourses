__author__ = 'pvarenik'


def test_del_first_contact(app):
    app.contact.delete_first_contact()