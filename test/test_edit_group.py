__author__ = 'pvarenik'
from model.group import Group
from random import randrange


def test_edit_some_group(app):
    if app.contact.count() == 0:
        app.group.create(Group(name="testgroup", header="New Group", footer="End of new group"))
    old_groups = app.group.get_group_list()
    group = Group(name="testgroup_edit", header="New Group Edit", footer="End of new group edit")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

