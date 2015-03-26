__author__ = 'pvarenik'
from model.group import Group

def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="testgroup", header="New Group", footer="End of new group"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups