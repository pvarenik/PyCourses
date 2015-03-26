__author__ = 'pvarenik'
from model.group import Group
from random import randrange


def test_del_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="testgroup", header="New Group", footer="End of new group"))
    old_groups = app.group.get_group_list()
    index = randrange(0, len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups