# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="Admin", password="secret")
    app.create_account(Contact("first", "middle", "last", "nick"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="Admin", password="secret")
    app.create_account(Contact("", "", "", ""))
    app.session.logout()