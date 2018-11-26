# -*- coding: utf-8 -*-
import random
import time

from model.contact import Contact


def test_del_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.open_contact_page()
        contact = Contact(firstname="fdfd", middlename="dd", lastname="ssd", nickname="dfd", title="fd",
                          company="gg", address="dds", home="sfs", mobile="sdsd", work="sdfd", fax="tt",
                          email="sffs",
                          email2="sdff", email3="s", homepage="dsfdsfd", bday="1", bmonth="February",
                          byear="44", aday="2", amonth="February", ayear="4545", address2="gergt",
                          phone2="ergth",
                          notes="trt")
        app.contact.create_contact(contact)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(5)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contsct_list(),
                                                                     key=Contact.id_or_max)
