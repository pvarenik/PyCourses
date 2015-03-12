# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="Admin", password="secret")
    app.create_account(Contact("first", "middle", "last", "nick"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="Admin", password="secret")
    app.create_account(Contact("", "", "", ""))
    app.logout()