__author__ = 'pvarenik'
from model.contact import Contact

def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact("first", "middle", "last", "nick"))
    group = orm.get_group_list()[0]
    old_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    old_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.add_to_group(old_contacts_not_in_group[0], group)
    new_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    assert len(old_contacts_not_in_group) == len(new_contacts_not_in_group) + 1
    assert len(old_contacts_in_group) == len(new_contacts_in_group) - 1

def test_delete_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact("first", "middle", "last", "nick"))
    groups  = orm.get_group_list()
    if len(groups) == 0:
        test_add_contact_to_group(app, orm)
    group = groups[0]
    old_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    old_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.delete_from_group(old_contacts_in_group[0], group)
    new_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    assert len(old_contacts_not_in_group) == len(new_contacts_not_in_group) - 1
    assert len(old_contacts_in_group) == len(new_contacts_in_group) + 1