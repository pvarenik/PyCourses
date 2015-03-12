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
    app.session.login(username="Admin", password="secret")
    app.group.create(Group(name="testgroup", header="New Group", footer="End of new group"))
    app.session.logout()


def test_empty_addGroup(app):
    app.session.login(username="Admin", password="secret")
    app.group.create(Group(name="", header="" , footer=""))
    app.session.logout()