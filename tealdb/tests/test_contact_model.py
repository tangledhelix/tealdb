from django.test import TestCase

from django.db.utils import IntegrityError

from tealdb.models import Contact, Site


class ContactModelTest(TestCase):

    def make_site(name=''):
        site = Site(name=name)
        site.save()
        return site

    def test_saving_and_retrieving_items(self):
        first_site = self.make_site()
        second_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=second_site)
        second_contact.save()

        third_contact = Contact(site=second_site)
        third_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts.count(), 3,
                         msg='Incorrect number of records saved')

        with self.assertRaises(IntegrityError,
                               msg='Missing site should raise exception'):
            fourth_contact = Contact()
            fourth_contact.save()

    def test_first_name(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, first_name='Daniel')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].first_name, '',
                         msg='Contact first_name has wrong default')
        self.assertEqual(saved_contacts[1].first_name, 'Daniel',
                         msg='Contact first_name saved incorrectly')

    def test_last_name(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, last_name='Lowe')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].last_name, '',
                         msg='Contact last_name has wrong default')
        self.assertEqual(saved_contacts[1].last_name, 'Lowe',
                         msg='Contact last_name saved incorrectly')

    def test_address1(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site,
                                 address1='123 Mockingbird Lane')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].address1, '',
                         msg='Contact address1 has wrong default')
        self.assertEqual(saved_contacts[1].address1, '123 Mockingbird Lane',
                         msg='Contact address1 saved incorrectly')

    def test_address2(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, address2='Suite 234')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].address2, '',
                         msg='Contact address2 has wrong default')
        self.assertEqual(saved_contacts[1].address2, 'Suite 234',
                         msg='Contact address2 saved incorrectly')

    def test_city(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, city='Cleveland')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].city, '',
                         msg='Contact city has wrong default')
        self.assertEqual(saved_contacts[1].city, 'Cleveland',
                         msg='Contact city saved incorrectly')

    def test_state(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, state='Ohio')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].state, '',
                         msg='Contact state has wrong default')
        self.assertEqual(saved_contacts[1].state, 'Ohio',
                         msg='Contact state saved incorrectly')

    def test_postal_code(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, postal_code='44060')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].postal_code, '',
                         msg='Contact postal_code has wrong default')
        self.assertEqual(saved_contacts[1].postal_code, '44060',
                         msg='Contact postal_code saved incorrectly')

    def test_country(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, country='United States')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].country, '',
                         msg='Contact country has wrong default')
        self.assertEqual(saved_contacts[1].country, 'United States',
                         msg='Contact country saved incorrectly')

    def test_phone(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, phone='216-555-1234')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].phone, '',
                         msg='Contact phone has wrong default')
        self.assertEqual(saved_contacts[1].phone, '216-555-1234',
                         msg='Contact phone saved incorrectly')

    def test_fax(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, fax='216-555-1234')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].fax, '',
                         msg='Contact fax has wrong default')
        self.assertEqual(saved_contacts[1].fax, '216-555-1234',
                         msg='Contact fax saved incorrectly')

    def test_mobile_phone(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, mobile_phone='216-555-1234')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].mobile_phone, '',
                         msg='Contact mobile_phone has wrong default')
        self.assertEqual(saved_contacts[1].mobile_phone, '216-555-1234',
                         msg='Contact mobile_phone saved incorrectly')

    def test_email(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, email='foo@foobar.com')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].email, '',
                         msg='Contact email has wrong default')
        self.assertEqual(saved_contacts[1].email, 'foo@foobar.com',
                         msg='Contact email saved incorrectly')

    def test_social_twitter(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, social_twitter='foobar')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].social_twitter, '',
                         msg='Contact social_twitter has wrong default')
        self.assertEqual(saved_contacts[1].social_twitter, 'foobar',
                         msg='Contact social_twitter saved incorrectly')

    def test_social_facebook(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, social_facebook='foobar')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].social_facebook, '',
                         msg='Contact social_facebook has wrong default')
        self.assertEqual(saved_contacts[1].social_facebook, 'foobar',
                         msg='Contact social_facebook saved incorrectly')

    def test_social_instagram(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, social_instagram='foobar')
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].social_instagram, '',
                         msg='Contact social_instagram has wrong default')
        self.assertEqual(saved_contacts[1].social_instagram, 'foobar',
                         msg='Contact social_instagram saved incorrectly')

    def test_asshole(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, asshole=True)
        second_contact.save()

        third_contact = Contact(site=first_site, asshole=False)
        third_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].asshole, False,
                         msg='Contact asshole has wrong default')
        self.assertEqual(saved_contacts[1].asshole, True,
                         msg='Contact asshole was not set correctly')
        self.assertEqual(saved_contacts[2].asshole, False,
                         msg='Contact asshole was not un-set correctly')

    def test_official(self):
        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, official=True)
        second_contact.save()

        third_contact = Contact(site=first_site, official=False)
        third_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].official, False,
                         msg='Contact official has wrong default')
        self.assertEqual(saved_contacts[1].official, True,
                         msg='Contact official was not set correctly')
        self.assertEqual(saved_contacts[2].official, False,
                         msg='Contact official was not un-set correctly')

    def test_notes(self):
        lorem_text = """
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
"""

        first_site = self.make_site()

        first_contact = Contact(site=first_site)
        first_contact.save()

        second_contact = Contact(site=first_site, notes=lorem_text)
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts[0].notes, '',
                         msg='Contact notes had wrong default value')
        self.assertEqual(saved_contacts[1].notes, lorem_text,
                         msg='Contacts notes did not save correctly')
