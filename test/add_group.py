# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_addGroup(app):
    app.login(username="Admin", password="secret")
    app.create_group(Group(name="testgroup", header="New Group", footer="End of new group"))
    app.logout()


def test_empty_addGroup(app):
    app.login(username="Admin", password="secret")
    app.create_group(Group(name="", header="" , footer=""))
    app.logout()