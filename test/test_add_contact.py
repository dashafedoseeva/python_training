# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    app.open_home_page()
    old_contacts = db.get_contact_list()
    app.contact.create_contact(contact)
    app.open_home_page()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
