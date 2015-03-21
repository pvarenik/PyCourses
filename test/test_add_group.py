# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="testgroup", header="New Group", footer="End of new group"))

def test_empty_add_group(app):
    app.group.create(Group(name="", header="" , footer=""))