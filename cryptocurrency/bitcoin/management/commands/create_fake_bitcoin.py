"""
Command for creating fake bitcoin instances when building
docker-compose to grab them with celery task and updating them.
"""
from django.core.management.base import BaseCommand

from ...models import Bitcoin


class Command(BaseCommand):
    help = 'creating fake bitcoin instances for using with celery tasks...'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):

        for i in range(1, 101):
            Bitcoin.objects.create(price=0)

        self.stdout.write(
            self.style.SUCCESS('Bitcoin Instances were created...')
        )
