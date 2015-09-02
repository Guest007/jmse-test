# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from optparse import make_option
from jmse.engine import get_jm_json

__author__ = 'guest007'

class Command(BaseCommand):
    help = "Load advertisers list from partner"
    option_list = BaseCommand.option_list + (
        make_option('--url',
            help='Set optional url'),
        # make_option('--token',
        #             help='Operations with token (new or refresh)'),
        # make_option('--check',
        #             help='Check links'),
    )

    def handle(self, *args, **options):
        get_jm_json(**options)
        # grab(*args, **options)


