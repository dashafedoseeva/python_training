# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_del_some_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.open_contact_page()
        contact = Contact(firstname="fdfd", middlename="dd", lastname="ssd", nickname="dfd", title="fd",
                          company="gg", address="dds", home="sfs", mobile="sdsd", work="sdfd", fax="tt",
                          email="sffs",
                          email2="sdff", email3="s", homepage="dsfdsfd", bday="1", bmonth="February",
                          byear="44", aday="2", amonth="February", ayear="4545", address2="gergt",
                          phone2="ergth",
                          notes="trt")
        app.contact.create_contact(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
