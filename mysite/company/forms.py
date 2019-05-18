from django import forms

class NameForm(forms.Form):
    your_name = forms.IntegerField(label='Quantity ', min_value=1, max_value=50)
