# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_contact_page()
    app.contact.create_contact(Contact(firstname="fdfd", middlename="dd", lastname="ssd", nickname="dfd", title="fd",
                                       company="gg", address="dds", home="sfs", mobile="sdsd", work="sdfd", fax="tt",
                                       email="sffs",
                                       email2="sdff", email3="s", homepage="dsfdsfd", bday="1", bmonth="February",
                                       byear="44", aday="2", amonth="February", ayear="4545", address2="gergt",
                                       phone2="ergth",
                                       notes="trt"))
    app.contact.return_to_home_page()
    app.session.logout()
