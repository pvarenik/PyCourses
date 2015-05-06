__author__ = 'pvarenik'
from model.group import Group
import random
import pytest


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testgroup", header="New Group", footer="End of new group"))
    with pytest.allure.step("Getting groups from DB"):
        old_groups = db.get_group_list()
    group = Group(name="1231321321321", header="New Group Editfdsfdsdf", footer="End of new group editsdfsdfsdfsdfdsf")
    group_to_edit = random.choice(old_groups)
    index = old_groups.index(group_to_edit)
    group.id = old_groups[index].id
    with pytest.allure.step("Edit group"):
        app.group.edit(group)
    with pytest.allure.step("Getting new groups from DB"):
        new_groups = db.get_group_list()
    old_groups[index] = group
    with pytest.allure.step("Verify that groups was edited"):
        if check_ui:
            assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

