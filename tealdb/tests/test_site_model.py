from django.test import TestCase

from tealdb.models import Site


class SiteModelTest(TestCase):

    def test_site_name(self):
        first_site = Site()
        first_site.save()

        second_site = Site(name='Terminal Tower')
        second_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].name, '',
                         msg='Site name did not have correct default value')
        self.assertEqual(saved_sites[1].name, 'Terminal Tower',
                         msg='Site name did not save correctly')

    def test_street_address(self):

        first_site = Site()
        first_site.save()

        second_site = Site(address1='50 Public Square',
                           address2='Unit 1')
        second_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].address1, '',
                         msg='Site address1 has wrong default value')
        self.assertEqual(saved_sites[0].address2, '',
                         msg='Site address2 has wrong default value')
        self.assertEqual(saved_sites[1].address1, '50 Public Square',
                         msg='Site address1 did not save correctly')
        self.assertEqual(saved_sites[1].address2, 'Unit 1',
                         msg='Site address2 did not save correctly')

    def test_city(self):
        first_site = Site()
        first_site.save()

        second_site = Site(city='Cleveland')
        second_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].city, '',
                         msg='Site city has wrong default value')
        self.assertEqual(saved_sites[1].city, 'Cleveland',
                         msg='Site city did not save correctly')

    def test_state(self):
        first_site = Site()
        first_site.save()

        second_site = Site(state='Ohio')
        second_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].state, '',
                         msg='Site state has wrong default value')
        self.assertEqual(saved_sites[1].state, 'Ohio',
                         msg='Site state did not save correctly')

    def test_postal_code(self):
        first_site = Site()
        first_site.save()

        second_site = Site(postal_code='44113')
        second_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].postal_code, '',
                         msg='Site postal_code has wrong default value')
        self.assertEqual(saved_sites[1].postal_code, '44113',
                         msg='Site postal_code did not save correctly')

    def test_country(self):
        first_site = Site()
        first_site.save()

        second_site = Site(country='United States')
        second_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].country, '',
                         msg='Site country has wrong default value')
        self.assertEqual(saved_sites[1].country, 'United States',
                         msg='Site country did not save correctly')

    def test_web_site(self):
        first_site = Site()
        first_site.save()

        second_site = Site(web_site='http://www.turnitteal.org')
        second_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].web_site, '',
                         msg='Site web_site has wrong default value')
        self.assertEqual(saved_sites[1].web_site,
                         'http://www.turnitteal.org',
                         msg='Site web_site did not save correctly')

    def test_email(self):
        first_site = Site()
        first_site.save()

        second_site = Site(email='terminaltower@terminaltower.org')
        second_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].email, '',
                         msg='Site email has wrong default value')
        self.assertEqual(saved_sites[1].email,
                         'terminaltower@terminaltower.org',
                         msg='Site email did not save correctly')

    def test_phone(self):
        first_site = Site()
        first_site.save()

        second_site = Site(phone='216-555-1234')
        second_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].phone, '',
                         msg='Site phone has wrong default value')
        self.assertEqual(saved_sites[1].phone, '216-555-1234',
                         msg='Site phone did not save correctly')

    def test_fax(self):
        first_site = Site()
        first_site.save()

        second_site = Site(fax='216-555-1234')
        second_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].fax, '',
                         msg='Site fax has wrong default value')
        self.assertEqual(saved_sites[1].fax, '216-555-1234',
                         msg='Site fax did not save correctly')

    def test_have_lit(self):
        first_site = Site()
        first_site.save()

        second_site = Site(have_lit=True)
        second_site.save()

        third_site = Site(have_lit=False)
        third_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].have_lit, False,
                         msg='Site have_lit has wrong default value')
        self.assertEqual(saved_sites[1].have_lit, True,
                         msg='Site have_lit did not save as set')
        self.assertEqual(saved_sites[2].have_lit, False,
                         msg='Site have_lit did not save as un-set')

    def test_years_lit(self):
        first_site = Site()
        first_site.save()

        second_site = Site(years_lit='2014-2016')
        second_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].years_lit, '',
                         msg='Site years_lit has wrong default value')
        self.assertEqual(saved_sites[1].years_lit, '2014-2016',
                         msg='Site years_lit did not save correctly')

    def test_map_link(self):
        map_link = 'https://www.google.com/maps/place/Renaissance+Hotel/' + \
            '@41.4983861,-81.696354,17z/data=!3m1!5s0x8830f07f00f' + \
            '506af:0x7edf0a3a8d9b543c!4m13!1m7!3m6!1s0x8830f07fb2' + \
            'd7d819:0xf82ec23face9fb6!2sTerminal+Tower!3b1!8m2!3d' + \
            '41.4983861!4d-81.6941653!3m4!1s0x8830f07e4562d241:0x' + \
            '94e8396bc5227630!8m2!3d41.4986081!4d-81.6944752'

        first_site = Site()
        first_site.save()

        second_site = Site(map_link=map_link)
        second_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].map_link, '',
                         msg='Site map_link has wrong default value')
        self.assertEqual(saved_sites[1].map_link, map_link,
                         msg='Site map_link did not save correctly')

    def test_fee(self):
        first_site = Site()
        first_site.save()

        second_site = Site(fee=True)
        second_site.save()

        third_site = Site(fee=False)
        third_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].fee, False,
                         msg='Site fee has wrong default value')
        self.assertEqual(saved_sites[1].fee, True,
                         msg='Site fee did not save as set')
        self.assertEqual(saved_sites[2].fee, False,
                         msg='Site fee did not save as un-set')

    def test_disposition(self):
        first_site = Site()
        first_site.save()

        second_site = Site(disposition='not_contacted')
        second_site.save()

        third_site = Site(disposition='responded_lit')
        third_site.save()

        fourth_site = Site(disposition='responded_declined')
        fourth_site.save()

        fifth_site = Site(disposition='no_response')
        fifth_site.save()

        sixth_site = Site(disposition='contact_failed')
        sixth_site.save()

        sixth_site = Site(disposition='pending')
        sixth_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].disposition, 'not_contacted',
                         msg='Site disposition has wrong default value')
        self.assertEqual(saved_sites[1].disposition, 'not_contacted',
                         msg='Site disposition was saved incorrectly')
        self.assertEqual(saved_sites[2].disposition, 'responded_lit',
                         msg='Site disposition was saved incorrectly')
        self.assertEqual(saved_sites[3].disposition, 'responded_declined',
                         msg='Site disposition was saved incorrectly')
        self.assertEqual(saved_sites[4].disposition, 'no_response',
                         msg='Site disposition was saved incorrectly')
        self.assertEqual(saved_sites[5].disposition, 'contact_failed',
                         msg='Site disposition was saved incorrectly')
        self.assertEqual(saved_sites[6].disposition, 'pending',
                         msg='Site disposition was saved incorrectly')

    def test_notes(self):
        lorem_text = """
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
"""

        first_site = Site()
        first_site.save()

        second_site = Site(notes=lorem_text)
        second_site.save()

        saved_sites = Site.objects.all()
        self.assertEqual(saved_sites[0].notes, '',
                         msg='Site notes had wrong default value')
        self.assertEqual(saved_sites[1].notes, lorem_text,
                         msg='Site notes did not save correctly')
