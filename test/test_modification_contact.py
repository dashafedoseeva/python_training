# -*- coding: utf-8 -*-
def test_modification_contact(app):
    app.open_home_page()
    app.contact.open_contact_page()
    app.contact.modification_contact()
    app.contact.return_to_home_page()
