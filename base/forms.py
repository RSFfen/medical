from django import forms

class InputClientForm(forms.Form):
    input_client = forms.CharField(required=True, max_length=50, label='Фамилия',
        widget=forms.TextInput(
        attrs={
            'class': 'basicAutoComplete',
            'data-url': '/client_autocomplete/'
        }))