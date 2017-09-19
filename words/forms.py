from django.forms import ModelForm, CharField

from words.models import Word


class WordForm(ModelForm):
    wordExample = CharField(required=False)
    freeTrans = CharField(required=False)
    freeTransExample = CharField(required=False)
    freeTrans2 = CharField(required=False)
    freeTrans2Example = CharField(required=False)

    class Meta:
        model = Word
        fields = ['word']
