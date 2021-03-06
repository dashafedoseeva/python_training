# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_modification_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(
            Contact(firstname="fdfd", middlename="dd", lastname="ssd", nickname="dfd", title="fd",
                    company="gg", address="dds", home="sfs", mobile="sdsd", work="sdfd", fax="tt",
                    email="sffs",
                    email2="sdff", email3="s", homepage="dsfdsfd", bday="1", bmonth="February",
                    byear="44", aday="2", amonth="February", ayear="4545", address2="gergt",
                    phone2="ergth",
                    notes="trt"))
    app.open_home_page()
    contact = Contact(firstname='fff', lastname='ddd', address='ddddd')
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modification_contact_by_index(index, contact)
    app.open_home_page()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
