from django.forms import ModelForm
from .models import EntryModel

class EntryForm(ModelForm):
    class Meta:
        model = EntryModel
        fields = '__all__'