from django import forms
from .models import TodoList


class DataInput(forms.Form):

    item = forms.CharField(max_length=100)

    class Meta:
        model = TodoList
        fields = ['itemid', 'item']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].required = False
