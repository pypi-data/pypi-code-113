# -*- coding: utf-8 -*-
"""send newsletter"""

from datetime import datetime

from django.core.management.base import BaseCommand

from coop_cms.utils import send_newsletter
from coop_cms.models import NewsletterSending


class Command(BaseCommand):
    """send newsletter"""
    help = "send newsletter"

    def add_arguments(self, parser):
        """
        Entry point for subclassed commands to add custom arguments.
        """
        parser.add_argument('email_addresses')

    def handle(self, *args, **options):
        """command"""
        # look for emailing to be sent

        verbose = options.get('verbosity', 1)
        email_addresses = options.get('email_addresses', '')
        
        if email_addresses:
            email_list = email_addresses.split(";")
        else:
            print('usage: python manage.py send_newsletter toto@toto.fr;titi@titi.fr')
        
        sendings = NewsletterSending.objects.filter(scheduling_dt__lte=datetime.now(), sending_dt=None)
        for sending in sendings:
            if verbose:
                print('send_newsletter {1} to {0} addresses'.format(len(email_list), sending.newsletter))
            
            nb_sent = send_newsletter(sending.newsletter, email_list)
            
            if verbose:
                print(nb_sent, "emails sent")
            
            sending.sending_dt = datetime.now()
            sending.save()
