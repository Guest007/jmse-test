# -*- coding: utf-8 -*-
from django.test import TestCase

url = 'http://www.jm.se/bostader/sok-bostad/#c=stockholm&tab=objects&listmode=box'

class JMSETest(TestCase):

    def setUp(self):
        """
        set up our tests
        :return:
        """
        set.url = url

        return True

    def test_get_site_ok(self):
        pass
