# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.open_contact_page()
        app.contact.create_contact(
            Contact(firstname="fdfd", middlename="dd", lastname="ssd", nickname="dfd", title="fd",
                    company="gg", address="dds", home="sfs", mobile="sdsd", work="sdfd", fax="tt",
                    email="sffs",
                    email2="sdff", email3="s", homepage="dsfdsfd", bday="1", bmonth="February",
                    byear="44", aday="2", amonth="February", ayear="4545", address2="gergt",
                    phone2="ergth",
                    notes="trt"))
    app.contact.delete_first_contact()
