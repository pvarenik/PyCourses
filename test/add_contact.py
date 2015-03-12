# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="Admin", password="secret")
    app.contact.create(Contact("first", "middle", "last", "nick"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="Admin", password="secret")
    app.contact.create(Contact("", "", "", ""))
    app.session.logout()