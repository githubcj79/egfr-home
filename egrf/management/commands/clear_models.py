from django.core.management.base import BaseCommand
from crf.models import Subject, Variation, Entry

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _delete_objs(self):
		Entry.objects.all().delete()
		Variation.objects.all().delete()
		Subject.objects.all().delete()

    def handle(self, *args, **options):
        self._delete_objs()