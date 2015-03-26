__author__ = 'pvarenik'
from model.group import Group

def test_del_first_group(app):
    if app.contact.count() == 0:
        app.group.create(Group(name="testgroup", header="New Group", footer="End of new group"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups