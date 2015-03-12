# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="Admin", password="secret")
    app.group.create(Group(name="testgroup", header="New Group", footer="End of new group"))
    app.session.logout()


def test_empty_add_group(app):
    app.session.login(username="Admin", password="secret")
    app.group.create(Group(name="", header="" , footer=""))
    app.session.logout()