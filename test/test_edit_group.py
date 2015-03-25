__author__ = 'pvarenik'
from model.group import Group

def test_edit_first_group(app):
    if app.contact.count() == 0:
        app.group.create(Group(name="testgroup", header="New Group", footer="End of new group"))
    app.group.edit(Group(name="testgroup_edit", header="New Group Edit", footer="End of new group edit"))

