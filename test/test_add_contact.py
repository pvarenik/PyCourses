# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_str(prefix, maxlen):
    sym = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(sym) for i in range(random.randrange(maxlen))])

testdata = [Contact("", "", "", "")] + [
    Contact(name=random_str("name", 10), middlename=random_str("middlename", 10), lastname=random_str("lastname", 10), nickname=random_str("nickname", 10))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)