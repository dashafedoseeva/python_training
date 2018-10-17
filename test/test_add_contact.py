# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="fdfd", middlename="dd", lastname="ssd", nickname="dfd", title="fd",
                      company="gg", address="dds", home="sfs", mobile="sdsd", work="sdfd", fax="tt",
                      email="sffs",
                      email2="sdff", email3="s", homepage="dsfdsfd", bday="1", bmonth="February",
                      byear="44", aday="2", amonth="February", ayear="4545", address2="gergt",
                      phone2="ergth",
                      notes="trt")
    app.contact.create_contact(contact)
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.contact.return_to_home_page()
