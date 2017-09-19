from django.forms import ModelForm, CharField

from words.models import Word


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'prefix', 'stem', 'tone', 'POS', 'word_class', 'gloss', 'no', 'note', 'dialect']
