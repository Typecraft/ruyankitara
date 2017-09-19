from django.core.management import BaseCommand
from os import path

from words.models import Word


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(path.join(path.dirname(path.abspath(__file__)), 'lexicon'), 'r') as f:
            contents = f.readlines()[1:]
            contents = map(lambda x: x.split("\t"), contents)
            contents = map(lambda x: x + [''] * (10 - len(x)), contents)

            words = map(lambda x: Word(
                word=x[0],
                prefix=x[1],
                stem=x[2],
                tone=x[3],
                POS=x[4],
                word_class=x[5],
                gloss=x[6],
                no=int(x[7]),
                note=x[8],
                dialect=x[9]
            ), contents)
            Word.objects.bulk_create(words)
