__author__ = 'pvarenik'


def test_add_group(app):
    app.session.login(username="Admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()