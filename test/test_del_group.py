__author__ = 'pvarenik'
from model.group import Group
import random
import pytest


def test_del_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testgroup", header="New Group", footer="End of new group"))
    with pytest.allure.step("Getting groups from DB"):
        old_groups = db.get_group_list()
    group = random.choice(old_groups)
    with pytest.allure.step("Delete group with %s id" % group.id):
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step("Getting new groups from DB"):
        new_groups = db.get_group_list()
    #assert len(old_groups) - 1 == app.group.count()
    old_groups.remove(group)
    #assert old_groups == new_groups
    with pytest.allure.step("Verify that group was deleted"):
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)