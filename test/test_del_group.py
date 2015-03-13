__author__ = 'pvarenik'


def test_del_first_group(app):
    app.session.login(username="Admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()