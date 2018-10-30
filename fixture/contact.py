import re

from selenium.webdriver.support.select import Select

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("Enter")) > 0):
            wd.find_element_by_link_text("add new").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.contact.open_contact_page(index)

    def open_contact_view_by_details(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        # submit group creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.firstname)
        self.type("lastname", contact.lastname)
        self.type("home", contact.home)
        self.type("mobile", contact.mobile)
        self.type("work", contact.work)
        self.type("phone2", contact.phone2)
        self.type("email", contact.email)


    def type(self, field_firstname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_firstname).click()
            wd.find_element_by_name(field_firstname).clear()
            wd.find_element_by_name(field_firstname).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def modification_first_contact(self, new_contact_date):
        self.modification_contact_by_index(0)

    def modification_contact_by_index(self, index, new_contact_date):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_contact_by_index(index)
        # fill group form
        self.fill_contact_form(new_contact_date)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count_contact(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                last_name = element.find_elements_by_tag_name("td")[1].text
                first_name = element.find_elements_by_tag_name("td")[2].text
                address = element.find_elements_by_tag_name("td")[3].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_emails = element.find_elements_by_tag_name("td")[4].text
                all_phones = element.find_elements_by_tag_name("td")[5].text
                self.contact_cache.append(
                    Contact(firstname=first_name, lastname=last_name, address=address,
                            all_emails_from_home_page=all_emails, id=id, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute('value')
        lastname = wd.find_element_by_name("lastname").get_attribute('value')
        address = wd.find_element_by_name("address").get_attribute('value')
        id = wd.find_element_by_name("id").get_attribute('value')
        homephone = wd.find_element_by_name("home").get_attribute('value')
        workphone = wd.find_element_by_name("work").get_attribute('value')
        mobilephone = wd.find_element_by_name("mobile").get_attribute('value')
        secondaryphone = wd.find_element_by_name("phone2").get_attribute('value')
        email_first = wd.find_element_by_name("email").get_attribute('value')
        email_second = wd.find_element_by_name("email2").get_attribute('value')
        email_third = wd.find_element_by_name("email3").get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email=email_first, email2=email_second, email3=email_third,
                       home=homephone, mobile=mobilephone,
                       work=workphone,
                       phone2=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_view_by_details(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(home=homephone, mobile=mobilephone, work=workphone,
                       phone2=secondaryphone)
