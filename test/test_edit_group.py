__author__ = 'pvarenik'
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="Admin", password="secret")
    app.group.edit(Group(name="testgroup_edit", header="New Group Edit", footer="End of new group edit"))
    app.session.logout()