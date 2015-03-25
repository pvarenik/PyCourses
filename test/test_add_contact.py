# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact("first", "middle", "last", "nick"))

def test_add_empty_contact(app):
    app.contact.create(Contact("", "", "", ""))