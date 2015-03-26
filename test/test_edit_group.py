__author__ = 'pvarenik'
from model.group import Group

def test_edit_first_group(app):
    if app.contact.count() == 0:
        app.group.create(Group(name="testgroup", header="New Group", footer="End of new group"))
    old_groups = app.group.get_group_list()
    group = Group(name="testgroup_edit", header="New Group Edit", footer="End of new group edit")
    group.id = old_groups[0].id
    app.group.edit(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

